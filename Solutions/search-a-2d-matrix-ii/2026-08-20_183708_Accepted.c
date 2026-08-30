# Problem: Search a 2D Matrix II
# Status: Accepted
# Language: c
# Runtime: 48 ms
# Memory: 12.7 MB
# Submitted: 2026-08-20_183708 UTC
# URL: https://leetcode.com/submissions/detail/2114346819/



bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int i=0, j= *matrixColSize-1;
    while( i<matrixSize & j>=0){
        if(matrix[i][j] == target)
            return true;
        if(matrix[i][j]>target)
            j--;
        else
            i++;
    }
    return false;
}