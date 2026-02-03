#include <stdio.h>
#include <stdlib.h>

#define SEED 42

/* A program to generate random numbers. */
int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("USAGE: %s <total_nums> <max_num>\n", argv[0]);
        exit(1);
    }
    
    int total_num = atoi(argv[1]);
    int max_num = atoi(argv[2]);
    
    FILE *file = fopen("numbers.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    srand(SEED);
    if (file) {
        fprintf(file, "\xEF\xBB\xBF");
        for (int i = 0; i < total_num; i++) {
            fprintf(file, "%d\n", rand() % max_num);
        }
        fclose(file);
    }
    
    return 0;
}