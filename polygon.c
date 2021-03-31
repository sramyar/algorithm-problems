#include<stdio.h>
#include<stdlib.h>

FILE* openFile(void)
{
    // initialize and assign file pointer
    FILE *ifp;
    ifp = fopen("poly1.txt","r");
    return ifp;
}


void readParams(int* rows, int* cols, int* poly, int* fill, int* x, int* y)
{
    
    FILE *ifp = openFile();

    // initiating cursors and counter
    int counter = 0;
    int cue;

    // while loop for reading in the ints
    while (counter < 6){
        // read in number from file to cue
        fscanf(ifp, "%d", &cue);
        // cases for assigning the first numbers to coresp. params
        switch (counter)
        {
        case 0:
            *rows = cue;
            break;
        case 1:
            *cols = cue;
            break;
        case 2:
            *poly = cue;
            break;
        case 3:
            *fill = cue;
            break;
        case 4:
            *x = cue;
            break;
        case 5:
            *y = cue;
            break;
        }
        counter++; 
    }

}

void readImage(int rows, int cols, int** matrix)
{
    // initiate file pointer
    FILE *ifp = openFile();

    // setting cue, counter and i,j coordinates for matrix
    int cue;
    int counter, i, j;
    counter = i = j = 0;
    while (fscanf(ifp, "%d", &cue) != EOF){
        if (counter < 6) {;}
        else{
            matrix[i][j] = cue;
            if (j < cols -1){
                j++;
            }
            else{
                j = 0;
                i++;
            }
        }
        counter++;
    }
}

void changeColor(int** matrix, int fill, int poly, int x, int y, int rows, int cols)
{
    if (matrix[x][y] == fill || matrix[x][y] == poly){
        return;
    }

    matrix[x][y] = fill;
    if (x + 1 < cols){changeColor(matrix, fill, poly, x + 1, y, rows, cols);}
    if (x - 1 > 0){changeColor(matrix, fill, poly, x - 1, y, rows, cols);}
    if (y + 1 < rows){changeColor(matrix, fill, poly, x, y + 1, rows, cols);}
    if (y - 1 > 0){changeColor(matrix, fill, poly, x, y - 1, rows, cols);}
}


int main(void)
{

    // define parameters
    int rows, cols, poly, fill, x, y;
    readParams(&rows, &cols, &poly, &fill, &x, &y);
    int** matrix;
    matrix = (int**) malloc(rows*sizeof(int*));
    for (int i = 0; i < rows; i++){
        matrix[i] = (int*) malloc(cols*sizeof(int));
    }
    readImage(rows, cols, matrix);

    changeColor(matrix, fill, poly, x, y, rows, cols);

    for (size_t i = 0; i < rows; i++)
    {
        printf("\n");
        for (size_t j = 0; j < cols; j++)
        {
            printf("%d\t",matrix[i][j]);
        }
        
    }

    for (int i = 0; i < rows; i++)
    {
        free(matrix[i]);
    }
    

    return 0;

}