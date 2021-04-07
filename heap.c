#include<stdlib.h>
#include<stdio.h>

// Implementation of (Max) Heap

// Helper funcs for fetching parent and left/right child
int parent(int i)
{
    return i/2;
}

int left(int i)
{
    return 2*i;
}

int right(int i)
{
    return 2*i + 1;
}

// Helper for replacing A[i] and A[j] elements in an array
void swap(int* A, int i, int j)
{
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

// Helper for printing an array
void printArray(int* A, int size)
{
    printf("[ ");
    for (size_t i = 0; i < size; i++)
    {
        printf("%d, ",A[i]);
    }
    printf(" ]\n");
    
}

// declare Heap struct
typedef struct Heap {int length; int size; int* array;} Heap;

// Heap constructor; only initializes
Heap* initializeHeap(int len, int h_size, int* arr)
{
    Heap* h = malloc(sizeof(Heap));
    h->array = arr;
    h->size = h_size;
    h->length = len;
    return h;
}

// Maintain Heap property given an index i for heal A
void heapify(Heap* h, int i)
{
    int largest;
    int l = left(i);
    int r = right(i);
    if (l < h->size && h->array[l] > h->array[i]){
        largest = l;
    }
    else{
        largest = i;
    }
    if (r < h->size && h->array[r] > h->array[largest]){
        largest = r;
    }
    if (largest != i){
        swap(h->array, i, largest);
        heapify(h, largest);
    }
}

// Build heap
Heap* array_to_Heap(int* A, int len)
{
    Heap* h = initializeHeap(len, len, A);
    for (int i = h->length/2 ; i >= 0; i--){
        heapify(h,i);
    }
    return h;
}

int main(void)
{
    int arr[10] = {16,4,10,14,7,9,3,2,8,1};
    Heap* h = array_to_Heap(arr,10);
    printArray(h->array, h->length);
    // Heap* A = initializeHeap(10,10,arr);
    // printArray(A->array, A->length);
    // heapify(A, 1);
    // printArray(A->array, A->length);
    

    // int A[4] = {1,2,3,4};
    // printArray(A,4);
    // swap(A,1,2);
    // printArray(A,4);
    // int parnt = parent(3);
    // int lef = left(3);
    // int righ = right(3);
    // printf("parent: %d, left: %d, right: %d\n",parnt,lef,righ);

    return 0;
}