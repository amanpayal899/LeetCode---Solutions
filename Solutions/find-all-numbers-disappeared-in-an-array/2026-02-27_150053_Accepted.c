# Problem: Find All Numbers Disappeared in an Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 37.2 MB
# Submitted: 2026-02-27_150053 UTC
# URL: https://leetcode.com/submissions/detail/1932867485/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    int *arr1 = (int*)calloc(numsSize,sizeof(int));
    int *result = (int*)calloc(numsSize,sizeof(int)) ;
    for(int i=0 ; i<numsSize ; i++){
        arr1[nums[i]-1] = 1;
    }

    int j=0 ;
    for(  int i=0 ; i<numsSize ; i++){
        if( arr1[i] == 0 ){
            result[j++] = i+1 ;
        }
    }
    free(arr1) ;
    *returnSize = j;
    return result ;
}