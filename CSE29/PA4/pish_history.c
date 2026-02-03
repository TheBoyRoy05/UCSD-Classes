#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#include "pish.h"

static char pish_history_path[1024] = {'\0'};

static void set_history_path() {
    const char* home = getpwuid(getuid())->pw_dir;
    strncpy(pish_history_path, home, 1024);
    strcat(pish_history_path, "/.pish_history");
}

void add_history(const struct pish_arg* arg) {
    if (!(*pish_history_path)) set_history_path();

    FILE *fp = fopen(pish_history_path, "a");
    if (fp == NULL) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < arg->argc; i++) {
        fprintf(fp, "%s ", arg->argv[i]);
    }

    fprintf(fp, "\n");
    fclose(fp);
}

void print_history() {
    if (!(*pish_history_path)) set_history_path();

    FILE *fp = fopen(pish_history_path, "r");
    if (fp == NULL) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    char buf[1024];
    int line = 0;
    while (fgets(buf, 1024, fp)) {
        printf("%d %s", line++, buf);
    }

    fclose(fp);
}
