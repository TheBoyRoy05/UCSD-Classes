#include "list.h"

#include <stdio.h>
#include <stdlib.h>

#define MAX_INTS 1000

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE* file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    unsigned char bom[3];
    fread(bom, 1, 3, file);
    if (!(bom[0] == 0xEF && bom[1] == 0xBB && bom[2] == 0xBF)) rewind(file);

    int* arr = malloc(MAX_INTS * sizeof(int));
    if (arr == NULL) {
        perror("Memory allocation failed");
        fclose(file);
        return 1;
    }

    int i = 0;
    while (i < MAX_INTS && fscanf(file, "%d", &arr[i]) == 1) i++;
    printf("\nArray: ");
    print_array(arr, i);
    fclose(file);

    struct node* head = create_list(arr, i);
    printf("Linked List: ");
    print_list(head);

    while (1) {
        printf("\nEnter a number to search (or 'q' to quit): ");

        int num;
        if (scanf("%d", &num) != 1) {
            while (getchar() != '\n');
            break;
        }

        int array_index = search_array(arr, i, num);
        if (array_index == -1)
            printf("Number not found in array.\n");
        else
            printf("Number found at index %d in array.\n", array_index);

        int list_index = search_list(head, num);
        if (list_index == -1)
            printf("Number not found in linked list.\n");
        else
            printf("Number found at index %d in linked list.\n", list_index);
    }

    struct node* sorted_head = create_sorted_list(head);
    printf("\nSorted Linked List: ");
    print_list(sorted_head);

    int* sorted_arr = malloc(MAX_INTS * sizeof(int));
    if (sorted_arr == NULL) {
        perror("Memory allocation failed");
        free(arr);
        free_list(head);
        free_list(sorted_head);
        return 1;
    }

    int len = copy_list_to_array(sorted_head, sorted_arr);
    printf("Sorted Array: ");
    print_array(sorted_arr, len);

    printf("\nOriginal Linked List: ");
    print_list(head);

    printf("Original Array: ");
    print_array(arr, i);

    FILE* output = fopen("sorted_numbers.txt", "w");
    if (output == NULL) {
        perror("Error opening file");
        free(arr);
        free(sorted_arr);
        free_list(head);
        free_list(sorted_head);
        return 1;
    }

    for (int i = 0; i < len; i++) {
        fprintf(output, "%d\n", sorted_arr[i]);
    }
    printf("\nNumber of integers written to the file: %d\n", len);

    free(arr);
    free(sorted_arr);
    free_list(head);
    free_list(sorted_head);
    fclose(output);

    return 0;
}

void free_list(struct node* head) {
    struct node* curr = head;
    while (curr != NULL) {
        struct node* next = curr->next;
        free(curr);
        curr = next;
    }
}

struct node* create_list(int intarray[], int len) {
    struct node* head = NULL;
    for (int i = len - 1; i >= 0; i--) {
        head = add_item_at_start(head, intarray[i]);
    }
    return head;
}

struct node* add_item_at_start(struct node* head, int data) {
    struct node* new_node = malloc(sizeof(struct node));
    if (new_node == NULL) {
        perror("Memory allocation failed");
        return NULL;
    }

    new_node->data = data;
    new_node->next = head;
    return new_node;
}

int search_list(struct node* head, int element) {
    int count = 1;
    struct node* curr = head;
    while (curr != NULL) {
        if (curr->data == element) return count;
        curr = curr->next;
        count++;
    }
    return -1;
}

int search_array(int integers[], int numints, int element) {
    for (int i = 0; i < numints; i++) {
        if (integers[i] == element) return i;
    }
    return -1;
}

int copy_list_to_array(struct node* head, int* array) {
    int count = 0;
    struct node* curr = head;
    while (curr != NULL) {
        array[count] = curr->data;
        curr = curr->next;
        count++;
    }
    return count;
}

struct node* create_sorted_list(struct node* head) {
    struct node* curr = head;
    struct node* sorted_head = NULL;
    while (curr != NULL) {
        sorted_head = add_item_sorted(sorted_head, curr->data);
        curr = curr->next;
    }
    return sorted_head;
}

struct node* add_item_sorted(struct node* sorted_head, int data) {
    struct node* new_node = malloc(sizeof(struct node));
    if (new_node == NULL) {
        perror("Memory allocation failed");
        return NULL;
    }
    new_node->data = data;

    struct node* curr = sorted_head;
    if (curr == NULL || curr->data >= data) {
        new_node->next = sorted_head;
        return new_node;
    }

    while (curr->next != NULL && curr->next->data < data) curr = curr->next;
    new_node->next = curr->next;
    curr->next = new_node;
    return sorted_head;
}

void print_list(struct node* head) {
    if (head == NULL) {
        printf("Linked List is Empty.\n");
    } else {
        struct node* temp = head;
        printf("head->");
        while (temp != NULL) {
            printf("|%d|->", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}

void print_array(int integers[], int len) {
    printf("[");
    for (int i = 0; i < len; i++) {
        if (i > 0)
            printf(", ");
        printf("%d", integers[i]);
    }
    printf("]\n");
}