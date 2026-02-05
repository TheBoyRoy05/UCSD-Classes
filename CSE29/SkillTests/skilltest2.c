#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

struct node* add_item_at_pos(struct node* head, int data, int pos) {
    struct node* new_node = malloc(sizeof(struct node));
    if (new_node == NULL) {
        perror("Memory allocation failed");
        return NULL;
    }
    new_node->data = data;

    int count = 1;
    struct node* curr = head;
    if (curr == NULL || count >= pos) {
        new_node->next = curr;
        return new_node;
    }

    while (curr->next != NULL && count < pos) {
        if (count == pos) {
            new_node->next = curr->next;
            curr->next = new_node;
            return head;
        }
        curr = curr->next;
        count++;
    }

    new_node->next = NULL;
    curr->next = new_node;
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

struct node* create_list(int intarray[], int len) {
    struct node* head = NULL;
    for (int i = len - 1; i >= 0; i--) {
        head = add_item_at_start(head, intarray[i]);
    }
    return head;
}

void free_list(struct node* head) {
    struct node* curr = head;
    while (curr != NULL) {
        struct node* next = curr->next;
        free(curr);
        curr = next;
    }
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

int main() {
    int test1[] = {1, 2, 3};
    struct node* head1 = create_list(test1, 3);
    print_list(head1);
    head1 = add_item_at_pos(head1, 4, 1);
    print_list(head1);
    free_list(head1);

    int test2[] = {1, 2, 3, 4, 5};
    struct node* head2 = create_list(test2, 5);
    print_list(head2);
    head2 = add_item_at_pos(head2, 6, 10);
    print_list(head2);
    free_list(head2);
}