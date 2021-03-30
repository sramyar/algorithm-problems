#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int rows, cols, poly, fill, x, y;
    int** matrix;
    FILE *ifp, *ofp;
    char filename[20];
    //scanf("%s",filename);
    ifp = fopen("poly1.txt","r");
    //ofp = fopen(argv[2],"w");
    int counter, i, j = 0;
    int cue;
    while (fscanf(ifp, "%d", &cue) != EOF)
    {
        switch (counter)
        {
        case 0:
            rows = cue;
            matrix = (int**)malloc(rows*sizeof(int*));
            break;
        case 1:
            cols = cue;
            for (int j = 0; j < rows; j++){
                matrix[j] = (int*)malloc(cols*sizeof(int));
            }
            break;
        case 2:
            poly = cue;
            break;
        case 3:
            fill = cue;
            break;
        case 4:
            x = cue;
            break;
        case 5:
            y = cue;
            break;
        }
        
        counter++;
        
        if (counter > 6){
            matrix[i][j] = cue;
            //printf("%d%d",i,j);
            if (j < cols - 1)
            {
                j++;
            }
            else if(j == cols - 1)
            {
                i++;
                j = 0;
            }
        }
        

    }
    
    for (size_t i = 0; i < rows; i++)
    {
        printf("\n");
        for (size_t j = 0; j < cols; j++)
        {
            printf("%d\t",matrix[i][j]);
        }
        
    }
    
    
    
    

    return 0;
}