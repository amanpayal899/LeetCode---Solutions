# Problem: Running Sum of 1d Array
# Status: Accepted
# Language: c
# Runtime: 4 ms
# Memory: 11.2 MB
# Submitted: 2026-01-19_183352 UTC
# URL: https://leetcode.com/submissions/detail/1890243436/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int* runningSum=(int*)malloc(numsSize*sizeof(int));
    *returnSize=numsSize;
    
    for(int i=0;i<numsSize;i++){
        int sum=0;
        for(int j=0;j<=i;j++){
            sum=sum+nums[j];
        }
        runningSum[i]=sum;
    }
    return runningSum;
}