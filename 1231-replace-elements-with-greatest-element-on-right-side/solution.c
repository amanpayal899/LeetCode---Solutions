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
