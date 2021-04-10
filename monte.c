#include"queue.c"
//#include"heap.c"
#include"pqueue.c"



void generateArrival(Queue* q, Heap* h)
{
    //printf("h->size is: %d, h->length is: %d\n", h->size, h->length);
    //printf("pque elements: %d, queue elements: %d\n", h->size, q->count);
    if (h->size == q->count && h->size < h->length){
        int item = rand()%9 + 1;
        enqueue(q, item);
        insert(h, item);
    }
    // if(q->count < q->length - 1){
    //     int item = rand()%9 + 1;
    //     enqueue(q,item);
    // }
}

void processQueue(Queue* q, Heap* h, int* sumQ, int* sumPQ, int* processCount)
{
    if(rand()%3 == 0 && q->count > 0){
        // printArray(h->array, h->size);
        int x = extract_max(h);
        // printf("extracted max: %d\n", x);
        // printArray(h->array, h->size);
        (*sumPQ) += x;
        (*sumQ) += dequeue(q);
        (*processCount)++;
    }
    // if(rand()%3 == 0 && q->count > 0){
    //     (*valueSum) += dequeue(q);
    //     (*processCount)++;
    // }
}


int main(void)
{
    srand(5);
    int qarray[11] = {0};
    int harray[10] = {0};
  
    Heap* h = malloc(sizeof(Heap));
    //initializeHeap(h, 10, 0, harray);
    h = array_to_Heap(h, harray, 10, 0);
    Queue* q = initializeQueue(11,qarray);
    int sumQ = 0;
    int sumPQ = 0;
    int processCount = 0;
    int iters = 500000;
    for (int i = 0; i < iters; i++){
        generateArrival(q, h);
        //printArray(h->array,h->length);
        // printf("count is: %d\n", q->count);
        // printf("Arrived:\n");
        //printf("Queue is:\t");
        //printQueue(q);
        //printf("Priority Queue is:\t");
        //printArray(h->array,h->size);
        processQueue(q, h, &sumQ, &sumPQ, &processCount);
        // printf("Processed:\n");
        // printQueue(q);
        // printf("______________________________________\n");

    }


    printf("Average for Queue is: %f\n", (float)sumQ/processCount);
    printf("Average for Pririty Queue is: %f\n", (float)sumPQ/processCount);
    
    

    
    return 0;
}