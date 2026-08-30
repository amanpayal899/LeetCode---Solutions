# Problem: Concatenation of Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 14.4 MB
# Submitted: 2026-01-23_144132 UTC
# URL: https://leetcode.com/submissions/detail/1894415859/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
   int *ans = (int*)malloc(2*numsSize*sizeof(int));
   *returnSize=2*numsSize;
   int i=0;
   for(;i+numsSize<2*numsSize;i++){
      ans[i]=nums[i];
      ans[i+numsSize]=nums[i];
   } 
   return ans;
}