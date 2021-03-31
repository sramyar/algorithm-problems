#include<stdio.h>
#include<stdlib.h>


void cal(int** arr)
{
    for (int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            arr[i][j] = 121;
        }
        
    }
}

int main(void)
{
    int** arr;
    arr = (int**)malloc(3*sizeof(int*));
    for (int i = 0; i < 3; i++)
    {
        arr[i] = (int*)malloc(3*sizeof(int));
    }
    
    cal(arr);
    for (int i = 0; i < 3; i++){
        printf("\n");
        for(int j = 0; j < 3; j++){
            printf("%d\t", arr[i][j]);
        }
        
    }
    printf("\n");
    
    return 0;
}