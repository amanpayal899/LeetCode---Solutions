# Problem: Two Sum
# Status: Accepted
# Language: c
# Runtime: 199 ms
# Memory: 8.7 MB
# Submitted: 2026-01-08_180842 UTC
# URL: https://leetcode.com/submissions/detail/1879048265/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i=0;i<numsSize;i++){
        for(int j=0;j<numsSize;j++){
            if(j==i)
            continue;
            else if(nums[i]+nums[j]==target){
                int* result=(int*)malloc(2*sizeof(int));
                result[0]=i;
                result[1]=j;
                *returnSize=2;
                return result;
            }
            }
        }
        *returnSize=0;
        return NULL;
    }