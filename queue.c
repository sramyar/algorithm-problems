#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

// Implemeting Queue

// Signature
typedef struct Queue{int head; int tail; int length; int count; int* array;} Queue;


// Initializing Queue
Queue* initializeQueue(int n, int* arr)
{
    Queue* q = malloc(sizeof(Queue));
    q->array = arr;
    q->length = n;
    q->head = 0;
    q->tail = 0;
    q->count = 0;
    return q;
}

void enqueue(Queue* q, int x)
{
    assert(q->count < q->length - 1);
    (q->array)[q->tail] = x;
    if (q->tail == (q->length) - 1){
        q->tail = 0;
    }
    else{
        (q->tail)++;
    }
    (q->count)++;
}

int dequeue(Queue* q)
{
    assert(q->count > 0);
    int x = q->array[q->head];
    if (q->head == (q->length) - 1){
        (q->head) = 0;
    }
    else{
        (q->head)++;
    }
    (q->count)--;
    return x;
}

void printQueue(Queue* q)
{
    if(q->count == 0){printf("[ ]\n");}
    int cue = q->head;
    if(q->head < q->tail){
        while (cue < (q->tail))
        {
            printf("%d <-- ",q->array[cue]);
            cue++;
        }
        
    }
    else{
        for(int i=0; i < q->count - 1; i++){
            printf("%d <-- ", q->array[cue]);
            if(cue != q->length - 1){cue++;}
            else {cue = 0;}
        }
    }
    printf("\n");
}

void printArr(int* arr, int size)
{
    for(int i = 0; i < size; i++){
        printf("%d\t",arr[i]);
    }
    printf("\n");
}


int main(void)
{
    int arr[7] = {0};
    Queue* q = initializeQueue(7,arr);
    printArr(q->array, q->length);
    for (int i=0; i<6; i++){
        printQueue(q);
        enqueue(q,i);
    }
    printQueue(q);
    dequeue(q);
    dequeue(q);
    dequeue(q);
    dequeue(q);
    dequeue(q); 
    printQueue(q);
    enqueue(q,200);
    enqueue(q,744);
    printQueue(q);
    dequeue(q);
    printQueue(q);

    
    return 0;
}