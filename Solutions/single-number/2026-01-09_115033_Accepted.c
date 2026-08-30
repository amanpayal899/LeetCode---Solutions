# Problem: Single Number
# Status: Accepted
# Language: c
# Runtime: 1053 ms
# Memory: 9.4 MB
# Submitted: 2026-01-09_115033 UTC
# URL: https://leetcode.com/submissions/detail/1879716531/

int singleNumber(int* nums, int numsSize) {int n;
    for(int i=0;i<numsSize;i++){
        int count=0;
        for(int j=0;j<numsSize;j++){
            if(nums[i]==nums[j]){
                count++;
                }
            }
        if(count==1){
           return nums[i];
        }
    }
    return 0;
}
