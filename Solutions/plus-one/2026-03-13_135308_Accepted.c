# Problem: Plus One
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 10 MB
# Submitted: 2026-03-13_135308 UTC
# URL: https://leetcode.com/submissions/detail/1947051770/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
   
        digits[digitsSize-1] += 1;
    for(int i = digitsSize-1 ; i>0 ; i-- )
    {
        if( digits[i] == 10 )
        {
            digits[i] = 0 ;
            digits[i-1] += 1 ;
        }
    }
    if( digits[0] == 10)
    {
        int* new = (int*)malloc((digitsSize+1)*sizeof(int));
        *returnSize = digitsSize+1;
        new[0] = 1;
        new[1] = 0;
        for( int i = 2 ; i<=digitsSize ; i++)
        {
           new[i] = digits[i-1];
        }
        return new;
    }
    *returnSize = digitsSize;
    return digits;
}
    
    