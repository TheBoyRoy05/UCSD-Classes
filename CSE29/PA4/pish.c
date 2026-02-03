#include "pish.h"

#include <ctype.h>
#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/*
 * Batch mode flag. If set to 0, the shell reads from stdin. If set to 1,
 * the shell reads from a file from argv[1].
 */
static int script_mode = 0;

/*
 * Prints a prompt IF NOT in batch mode (see script_mode global flag),
 */
int prompt(void) {
    static const char prompt[] = {0xe2, 0x96, 0xb6, ' ', ' ', '\0'};
    if (!script_mode) {
        printf("%s", prompt);
        fflush(stdout);
    }
    return 1;
}

/*
 * Print usage error for built-in commands.
 */
void usage_error(void) {
    fprintf(stderr, "pish: Usage error\n");
    fflush(stdout);
}

/*
 * Break down a line of input by whitespace, and put the results into
 * a struct pish_arg to be used by other functions.
 *
 * @param command   A char buffer containing the input command
 * @param arg       Broken down args will be stored here.
 */
void parse_command(char* command, struct pish_arg* arg) {
    arg->argv[arg->argc = 0] = NULL;

    char* token = strtok(command, " \t\n");
    while (token) {
        arg->argv[arg->argc++] = token;
        token = strtok(NULL, " \t\n");
    }
}

/*
 * Run a command.
 *
 * Built-in commands are handled internally by the pish program.
 * Otherwise, use fork/exec to create child process to run the program.
 *
 * If the command is empty, do nothing.
 * If NOT in batch mode, add the command to history file.
 */
void run(struct pish_arg* arg) {
    if (arg->argc == 0) return;
    if (!script_mode) add_history(arg);

    if (strcmp(arg->argv[0], "cd") == 0) {
        if (arg->argc != 2) {
            usage_error();
            return;
        }
        if (chdir(arg->argv[1]) == -1) {
            perror("chdir");
            return;
        }
        return;
    }

    if (strcmp(arg->argv[0], "exit") == 0) {
        if (arg->argc != 1) {
            usage_error();
            return;
        }
        exit(EXIT_SUCCESS);
    } else if (strcmp(arg->argv[0], "history") == 0) {
        if (arg->argc != 1) {
            usage_error();
            return;
        }
        print_history();
        return;
    }

    pid_t pid = fork();
    if (pid == 0) {
        execvp(arg->argv[0], arg->argv);
        perror("pish");
        exit(EXIT_FAILURE);
    } else if (pid < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else {
        int status;
        waitpid(pid, &status, 0);
    }
}

/*
 * Frees all the strings in the argv array of a struct pish_arg.
 * After calling this function, the struct pish_arg will be in an invalid state.
 */
void free_arg(struct pish_arg* arg) {
    for (int i = 0; i < arg->argc; i++) {
        free(arg->argv[i]);
    }
    arg->argv[arg->argc = 0] = NULL;
}

/*
 * The main loop. Continuously reads input from a FILE pointer
 * (can be stdin or an actual file) until `exit` or EOF.
 */
int pish(FILE* fp) {
    char buf[1024];
    struct pish_arg arg;

    while (prompt() && fgets(buf, 1024, fp)) {
        parse_command(buf, &arg);
        run(&arg);
        free_arg(&arg);
    }

    return 0;
}

int main(int argc, char* argv[]) {
    FILE* fp;
    
    if (argc == 1) {
        fp = stdin;
    } else if (argc == 2) {
        fp = fopen(argv[1], "r");
        if (fp == NULL) {
            perror("open");
            exit(EXIT_FAILURE);
        }
    } else if (argc > 2) {
        usage_error();
        exit(EXIT_FAILURE);
    }

    pish(fp);
    
    if (fp != stdin) fclose(fp);
    return EXIT_SUCCESS;
}
