# Problem: Missing Number
# Status: Accepted
# Language: c
# Runtime: 12 ms
# Memory: 9.3 MB
# Submitted: 2026-02-16_151815 UTC
# URL: https://leetcode.com/submissions/detail/1921167703/

#include<stdlib.h>
int missingNumber(int* nums, int numsSize) {
    int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
qsort(nums,numsSize,sizeof(int),compare);
for(int i=0 ; i<numsSize ; i++){
    if(nums[i] != i)
    return (nums[i]-1);
}
return numsSize;
}