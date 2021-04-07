#include"heap.c"
#include<assert.h>

// returns largest element in heap/highest priority
int get_max(Heap* h)
{
    return h->array[0];
}

// extract max element in heap
int extract_max(Heap* h)
{
    assert(h->size > 0);
    int max = h->array[0];
    h->array[0] = h->array[h->size - 1];
    h->size --;
    heapify(h, 0);
    return max;
}

// increase priority/value of element i in the heap to new_value
void increase_priority(Heap* h, int i, int new_value)
{
    assert(h->array[i] <= new_value);
    h->array[i] = new_value;
    while (i > 0)
    {
        swap(h->array, i, parent(i));
        i = parent(i);
    }
    
}

// insert value/key to heap
void insert(Heap* h, int value)
{
    assert(h->length > h->size);
    h->size++;
    h->array[h->size - 1] = -1;
    increase_priority(h, h->size - 1, value);
}

int main(void)
{
    int arr[12] = {0,11,16,4,10,14,7,9,3,2,8,1};
    Heap* h = array_to_Heap(arr,12);
    printArray(h->array, h->length);
    int max = extract_max(h);
    printf("max is: %d\n",max);
    printArray(h->array,h->size);
    increase_priority(h, 1, 17);
    printArray(h->array,h->size);
    insert(h, 18);
    printArray(h->array,h->size);
    return 0;
}
