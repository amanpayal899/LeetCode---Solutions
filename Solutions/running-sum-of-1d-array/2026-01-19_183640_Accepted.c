# Problem: Running Sum of 1d Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 11.2 MB
# Submitted: 2026-01-19_183640 UTC
# URL: https://leetcode.com/submissions/detail/1890246345/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int* runningSum=(int*)malloc(numsSize*sizeof(int));
    *returnSize=numsSize;
    int sum=0;
    for(int i=0;i<numsSize;i++){
        sum=sum+nums[i];
        runningSum[i]=sum;
    }
    return runningSum;
}