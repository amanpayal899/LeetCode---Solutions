# Problem: Matrix Diagonal Sum
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.9 MB
# Submitted: 2026-02-06_132654 UTC
# URL: https://leetcode.com/submissions/detail/1910277978/

int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum = 0 ;
    for(int i = 0, j = 0 ; i < matSize ; i++,j++){
        sum = sum + mat[i][j] + mat[i][*matColSize - i - 1] ;
        if( j == *matColSize - i - 1)
        sum -= mat[i][j];
    }
    return sum;
}