# Problem: Replace Elements with Greatest Element on Right Side
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 64.3 MB
# Submitted: 2026-04-02_174652 UTC
# URL: https://leetcode.com/submissions/detail/1967058728/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    int *result = (int*)malloc(arrSize*sizeof(int));
    int idx=arrSize-1;
    result[idx]=-1;
    int max=arr[idx--];
    for( ; idx>=0; idx-- )
    {
        if( arr[idx+1]>=max )
        max=arr[idx+1];
        result[idx] = max;
    }
    *returnSize=arrSize;
    return result;
}