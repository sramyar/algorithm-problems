#include<stdlib.h>
#include<stdio.h>

// include graph.h

typedef struct graphObj{int n; int** matrix;} graphObj;
typedef graphObj* graph;


// Graph constructor
graph createGraph(int num)
{
    // allocating memory to graph
    graph g = (graph)malloc(sizeof(graphObj));
    
    // allocating memory for backbone matrix
    g->matrix = (int**)calloc(num,sizeof(int*));
    for(int i = 0; i < num; i++){
        g->matrix[i] = (int*)malloc(sizeof(int));
    }

    for(int i = 0; i < num; i++)
        for(int j = 0; j < num; j++)
            g->matrix[i][j] = 0;

    g->n = num;

    return g;
}


void addEdge(graph* g, int i, int j)
{
    if (i >= (*g)->n || j >= (*g)->n){
        printf("\nInvalid index\n");
        return;
    }
    (*g)->matrix[i][j] = 1;
}

void removeEdge(graph* g, int i, int j)
{
    if (i >= (*g)->n || j >= (*g)->n){
        printf("\nInvalid index\n");
        return;
    }
    (*g)->matrix[i][j] = 0;
}


int hasEdge(graph g, int i, int j)
{
    return g->matrix[i][j];
}

void printGraph(graph g)
{
    int n = g->n;
    for(int i = 0; i < n; i++){
        printf("\n");
        for(int j = 0; j < n; j++){
            printf("%5d",g->matrix[i][j]);
        }
    }
    printf("\n");
}









int main(void)
{
    printf("salam\n");
    graph g = createGraph(10);
    for(int i = 0; i < 10; i++){
        addEdge(&g, i, i);
    }
    printGraph(g);

    removeEdge(&g, 4, 4);
    removeEdge(&g, 1, 3);
    removeEdge(&g, 2, 2);
    removeEdge(&g, 3, 3);

    printGraph(g);

    return 0;
}