int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum = 0 ;
    for(int i = 0, j = 0 ; i < matSize ; i++,j++){
        sum = sum + mat[i][j] + mat[i][*matColSize - i - 1] ;
        if( j == *matColSize - i - 1)
        sum -= mat[i][j];
    }
    return sum;
}
