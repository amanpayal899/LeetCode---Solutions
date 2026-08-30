# Problem: Replace Elements with Greatest Element on Right Side
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-02_172520 UTC
# URL: https://leetcode.com/submissions/detail/1967034983/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    int *result = (int*)malloc(arrSize*sizeof(int));
    int i=0;
    for( ; i<arrSize-1; i++ )
    {
        int max=arr[i+1];
        for( int j=i+1; j<arrSize; j++ )
        {
            
            if(arr[j]>max)
            max=arr[j];
        }
        result[i]=max;
    }
    result[i]=-1;
    *returnSize=arrSize;
    return result;
}