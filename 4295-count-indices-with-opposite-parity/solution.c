/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countOppositeParity(int* nums, int numsSize, int* returnSize) {
    int* answer = (int*) malloc( numsSize*sizeof(int));
    for( int i=0; i<numsSize; i++ )
    {
        int even = nums[i]%2;
        int count=0;
        for( int j=i+1; j<numsSize; j++ )
        {
            if( nums[j]%2 != even )
                count++;
           
        }
        answer[i] = count;
    }
    *returnSize = numsSize;
    return answer;
}
