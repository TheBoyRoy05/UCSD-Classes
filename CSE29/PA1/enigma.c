#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_SIZE 26
#define NUM_ROTORS 8

/* Array of rotors */
const char* enigma_rotors[NUM_ROTORS+1] = {
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ", //0
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ", //1
    "AJDKSIRUXBLHWTMCQGZNPYFVOE", //2
    "BDFHJLCPRTXVZNYEIWGAKMUSQO", //3
    "ESOVPZJAYQUIRHXLNFTGKDCMWB", //4
    "UKLBEPXWJVFZIYGAHCMTONDRQS", //5
    "JPGVOUMFYQBENHZRDKASXLICTW", //6
    "NZJHGRCXMYSWBOUFAIVLPEKQDT", //7
    "FKQHTLXOCBJSPDZRAMEWNIUYGV"  //8
};

/*
 * Convert a space-separated string of rotor indices into
 * an integer array of rotor indices
 *
 * @param rotor_ind_str   Space-separated string of rotor indices
 * @param num_rotors      Number of rotors provided in the string
 * @return                Integer array of rotor indices
 */
int* parse_rotor_indices(char* rotor_ind_str, int num_rotors) {
    int* rotors = malloc(num_rotors * sizeof(int));
    if (rotors == NULL) return NULL;
    char* token = strtok(rotor_ind_str, " ");

    for (int i = 0; i < num_rotors; i++) {
        if (token == NULL) {
            free(rotors);
            return NULL;
        }
        int val = atoi(token);
        if (val == 0 && token[0] != '0') {
            free(rotors);
            return NULL;
        }

        rotors[i] = val;
        token = strtok(NULL, " ");
    }
    return rotors;
}

/*
 * Create a 2D array of integers where
 * each row represents a rotor
 *
 * @param rotors          Integer array of rotor indices
 * @param num_rotors      Number of rotors provided
 * @return                2D array where each row represents a rotor
 */
int** set_up_rotors(int* rotors, int num_rotors) {
    int** rotor_config = malloc(num_rotors * sizeof(int*));
    if (rotor_config == NULL) return NULL;

    for (int i = 0; i < num_rotors; i++) {
        rotor_config[i] = malloc(ALPHABET_SIZE * sizeof(int));
        if (rotor_config[i] == NULL) {
            for (int j = 0; j < i; j++) free(rotor_config[j]);
            free(rotor_config);
            return NULL;
        }

        for (int j = 0; j < ALPHABET_SIZE; j++) {
            rotor_config[i][j] = enigma_rotors[rotors[i]][j] - 'A';
        }
    }

    return rotor_config;
}

/*
 * Rotate each rotor to the right by the
 * given number of rotations
 *
 * @param rotor_config   2D array of rotors
 * @param rotations      Number of rotations
 * @param num_rotors     Number of rotors provided
 */
void rotate_rotors(int** rotor_config, int rotations, int num_rotors) {
    for (int i = 0; i < num_rotors; i++) {
        int* temp = malloc(ALPHABET_SIZE * sizeof(int));
        if (temp == NULL) return;

        for (int j = 0; j < ALPHABET_SIZE; j++) {
            int pos = ((j - rotations) % ALPHABET_SIZE + ALPHABET_SIZE) % ALPHABET_SIZE;
            temp[j] = rotor_config[i][pos];
        }

        free(rotor_config[i]);
        rotor_config[i] = temp;
    }
}

/*
 * Encrypt the given message
 *
 * @param message        Message to encrypt
 * @param rotor_config   2D array of rotors
 * @param num_rotors     Number of rotors provided
 * @return               Encrypted message
 */
char* encrypt(char *message, int** rotor_config, int num_rotors) {
    int len = strlen(message);
    char* encrypted = malloc((len + 1) * sizeof(char));
    if (encrypted == NULL) return NULL;
    strcpy(encrypted, message);

    for (int i = 0; i < num_rotors; i++) {
        for (int j = 0; j < len; j++) {
            if (encrypted[j] < 'A' || encrypted[j] > 'Z') continue;
            encrypted[j] = rotor_config[i][encrypted[j] - 'A'] + 'A';
        }
    }

    encrypted[len] = '\0';
    return encrypted;
}

/*
* Find the index of the given value in the given array
*
* @param arr     Array to search
* @param val      Value to find
* @return         Index of the value in the array
* @return         -1 if the value is not found
*/
int indexOf(int* arr, int val) {
    if (arr == NULL) return -1;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (arr[i] == val) return i;
    }
    return -1;
}

/*
 * Decrypt the given message
 *
 * @param message        Message to decrypt
 * @param rotor_config   2D array of rotors
 * @param num_rotors     Number of rotors provided
 * @return               Decrypted message
 */
char* decrypt(char *message, int** rotor_config, int num_rotors) {
    int len = strlen(message);
    char* decrypted = malloc((len + 1) * sizeof(char));
    if (decrypted == NULL) return NULL;
    strcpy(decrypted, message);

    for (int i = 0; i < num_rotors; i++) {
        for (int j = 0; j < len; j++) {
            if (decrypted[j] < 'A' || decrypted[j] > 'Z') continue;
            decrypted[j] = enigma_rotors[0][indexOf(rotor_config[i], decrypted[j] - 'A')];
        }
    }

    decrypted[len] = '\0';
    return decrypted;
}

/*
 * Print the configuration of the rotors (for debugging purposes)
 *
 * @param rotor_config   2D array of rotors
 * @param num_rotors     Number of rotors provided
*/
void print_rotor_config(int** rotor_config, int num_rotors, char mode) {
    for (int i = 0; i < num_rotors; i++) {
        for (int j = 0; j < ALPHABET_SIZE; j++) {
            if (mode == 'c') printf("%c", rotor_config[i][j] + 'A');
            else if (mode == 'd') printf("%d ", rotor_config[i][j]);
        }
        printf("\n");
    }
}

/*
 * Format of command line input:
 * ./enigma e "JAVA" 3 "1 2 4" 0
 * 
 *    e    - mode (e for encrypt, d for decrypt)
 * "JAVA"  - message
 *    3    - number of rotors to use
 * "1 2 4" - indices of rotors to use
 *    0    - number of rotations of the rotors
 */
int main(int argc, char* argv[]) {
    if (argc == 1) {
        printf("Format of command line input:\n");
        printf("./enigma e \"JAVA\" 3 \"1 2 4\" 0\n \n");
        printf("    e    - mode (e for encrypt, d for decrypt)\n");
        printf(" \"JAVA\"  - message\n");
        printf("    3    - number of rotors to use\n");
        printf(" \"1 2 4\" - indices of rotors to use\n");
        printf("    0    - number of rotations of the rotors\n");
        exit(1);
    } else if (argc != 6) {
        printf("Usage: ./enigma <mode> <message> <num_rotors> <rotor_indices> <rotations>\n");
        exit(1);
    }

    char mode = *argv[1];

    char* message = malloc(strlen(argv[2]) + 1);
    if (message == NULL) return 1;
    strcpy(message, argv[2]);
    strupr(message);

    int num_rotors = atoi(argv[3]);
    int* rotors = parse_rotor_indices(argv[4], num_rotors);
    if (rotors == NULL) {
        free(message);
        printf("Invalid rotor indices.\n");
        exit(1);
    }

    int rotations = atoi(argv[5]);

    int** rotor_config = set_up_rotors(rotors, num_rotors);
    if (rotor_config == NULL) {
        free(message);
        free(rotors);
        printf("Memory allocation failed for rotors.\n");
        exit(1);
    }

    rotate_rotors(rotor_config, rotations, num_rotors);
    // print_rotor_config(rotor_config, num_rotors, 'd');

    if (mode == 'e') {
        char* encrypted = encrypt(message, rotor_config, num_rotors);
        printf("Encrypted Message: %s\n", encrypted);
        free(encrypted);
    } else if (mode == 'd') {
        char* decrypted = decrypt(message, rotor_config, num_rotors);
        printf("Decrypted Message: %s\n", decrypted);
        free(decrypted);
    } else {
        printf("Invalid mode. Use 'e' for encrypt or 'd' for decrypt.\n");
    }

    for (int i = 0; i < num_rotors; i++) free(rotor_config[i]);
    free(rotor_config);
    free(rotors);
    free(message);

    exit(0);
}