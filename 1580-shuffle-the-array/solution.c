

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
int* result = (int*)malloc(numsSize*sizeof(int));
for(int i=0,j=n,k=0 ; i<numsSize ; i++){
    result[i++] = nums[k++] ;
    result[i] = nums[j++] ;
}
*returnSize = numsSize;
return result ;
}
