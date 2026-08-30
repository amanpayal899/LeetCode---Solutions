# Problem: Missing Number
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-16_151227 UTC
# URL: https://leetcode.com/submissions/detail/1921161807/

#include<stdlib.h>
int missingNumber(int* nums, int numsSize) {
    int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
qsort(nums,numsSize,sizeof(int),compare);
for(int i=0 ; i<numsSize-1 ; i++){
    if(nums[i+1]-nums[i] == 2)
    return (nums[i]+1);
}
return numsSize;
}