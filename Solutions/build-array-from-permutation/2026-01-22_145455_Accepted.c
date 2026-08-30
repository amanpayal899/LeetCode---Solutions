# Problem: Build Array from Permutation
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 14.8 MB
# Submitted: 2026-01-22_145455 UTC
# URL: https://leetcode.com/submissions/detail/1893374405/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize) {
    int *ans;
    ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize=numsSize;
    for(int i=0;i<numsSize;i++){
        ans[i] = nums[nums[i]];
    }
    return ans;
}