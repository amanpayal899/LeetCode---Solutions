# Problem: Concatenation of Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 14.3 MB
# Submitted: 2026-02-21_143010 UTC
# URL: https://leetcode.com/submissions/detail/1926408750/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int *ans = (int*)malloc(numsSize*2*sizeof(int)) ;
    *returnSize = 2*numsSize ;
    for(int i=0 ; i<numsSize ; i++){
        ans[i] = nums[i] ;
        ans[i+numsSize] = nums[i] ;
    }
    return ans;
}