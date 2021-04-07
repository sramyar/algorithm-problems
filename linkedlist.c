#include<stdio.h>
#include<stdlib.h>
//#include"List.h"
//#include<assert.h>

// Node struct

typedef struct Node {int data; struct Node* next;} Node;

// List struct

typedef struct List{Node* head; int length;} List;

// List Constructor
List* newList(void)
{
    List* lptr = malloc(sizeof(List));
    lptr->head = NULL;
    lptr->length = 0;
    return lptr;
}

// Node constructor
Node* newNode(int x)
{
    Node* nptr = malloc(sizeof(Node));
    nptr->data = x;
    nptr->next = NULL;
    return nptr;
}

void addElement(List* lptr, int x)
{
    
    if (lptr->length == 0){
        //Node* h = newNode(x);
        Node* new = newNode(x);
        lptr->head = new;
        
    }
    else{
        // get a cue
        Node* cue;
        cue = lptr->head;
        // get to last element
        while (cue->next != NULL){
            cue = cue->next;
        }
        Node* tail = newNode(x);
        //Node* tail = malloc(sizeof(Node));
        //tail->data = x;
        cue->next = tail;
    }

    lptr->length++;
    //return lptr;
}

void printList(List* lptr)
{
    Node* cue;
    while (cue != NULL){
        printf("%d-->", cue->data);
        cue = cue->next;
    }
    printf("\n");

}

int main(void)
{
    List* lptr = newList();
    addElement(lptr,1);
    addElement(lptr,10);
    addElement(lptr,100);
    addElement(lptr,1000);
    printList(lptr);
    return 0;
}