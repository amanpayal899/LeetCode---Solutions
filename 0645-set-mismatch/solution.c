/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    int *asc = (int*)calloc( numsSize,sizeof(int) ) ;
    int *result = (int*)malloc( 2*sizeof(int));
    for(int i=0 ; i<numsSize ; i++){
        if(asc[nums[i]-1] == 0 ){
            asc[nums[i]-1] = nums[i] ;
            nums[i] = 0;
        }
    }
    for( int i = 0 ; i<numsSize ; i++){
        if(asc[i]==0)
          result[1] = i+1 ;
        if(nums[i]!=0)
          result[0] = nums[i] ;
    }
    free(asc);
    *returnSize = 2;
    return result;

}
