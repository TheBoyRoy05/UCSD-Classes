#ifndef LIST_H
#define LIST_H

struct node {
    int data;
    struct node *next;
};

void free_list(struct node *head);
struct node *create_list(int intarray[], int len);
struct node *add_item_at_start(struct node *head, int data);
int search_array(int integers[], int numints, int element);
int search_list(struct node *head, int element);
struct node *create_sorted_list(struct node *head);
struct node *add_item_sorted(struct node *head, int data);
int copy_list_to_array(struct node *head, int *array);
void print_list(struct node *head);
void print_array(int integers[], int len);

#endif