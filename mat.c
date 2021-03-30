#include<stdlib.h>
#include<stdio.h>

int main(void)
{
    int m[4][4];
    for (size_t i = 0; i < 4; i++)
    {
        for (size_t j = 0; j < 4; j++)
        {
            m[i][j] = 12;
        }
        
    }

    for (size_t i = 0; i < 4; i++)
    {
        printf("\n");
        for (size_t j = 0; j < 4; j++)
        {
            printf("%d\t",m[i][j]);
        }
    
    }
    printf("\n");
}