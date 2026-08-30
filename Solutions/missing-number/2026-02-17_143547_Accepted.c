# Problem: Missing Number
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.9 MB
# Submitted: 2026-02-17_143547 UTC
# URL: https://leetcode.com/submissions/detail/1922227946/

int missingNumber(int* nums, int numsSize) {
    int sum1 = 0,sum2 = 0;
    for(int i = 0 ; i<numsSize ; i++){
        sum1 += i+1 ;
        sum2 += nums[i] ;
    }
    return sum1-sum2 ;
    
}