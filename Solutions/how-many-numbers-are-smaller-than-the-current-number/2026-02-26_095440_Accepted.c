# Problem: How Many Numbers Are Smaller Than the Current Number
# Status: Accepted
# Language: c
# Runtime: 10 ms
# Memory: 11.2 MB
# Submitted: 2026-02-26_095440 UTC
# URL: https://leetcode.com/submissions/detail/1931684467/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    int *result = (int*)malloc(numsSize*sizeof(int)) ;
    for( int i=0 ; i<numsSize ; i++){
        int count = 0 ;
        for( int j=0 ; j<numsSize ; j++ ){
            if( nums[j] < nums[i] )
            count++;
        }
        result[i] = count ;
    } 
    *returnSize = numsSize;
    return result;
}