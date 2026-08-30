# Problem: Convert 1D Array Into 2D Array
# Status: Accepted
# Language: c
# Runtime: 8 ms
# Memory: 60.7 MB
# Submitted: 2026-03-15_091605 UTC
# URL: https://leetcode.com/submissions/detail/1948927939/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int** returnColumnSizes) {
    if( originalSize != m*n )
    {
        *returnSize = 0 ;
        return NULL ;
    }
    *returnSize = m ;
    *returnColumnSizes = (int*)malloc(m*sizeof(int));
    int **result = (int**)malloc( m*sizeof(int*)) ;
    for( int i=0 ; i<m ; i++ )
    {
        result[i] = (int*)malloc( n*sizeof(int)) ;
        (*returnColumnSizes)[i] = n;
    }
    for( int i=0 ; i<m ; i++ )
    {
        for( int j=0 ; j<n ; j++ )
        {
            result[i][j] = original[i*n+j] ;
        }
    }
    return result ;
}