# Problem: First Missing Positive
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-03_051121 UTC
# URL: https://leetcode.com/submissions/detail/1936328467/

int firstMissingPositive(int* nums, int numsSize) {
    int mis = 1;
    for( int i = 0 ; i<numsSize ;){
        if( nums[i] == mis){
           mis++;
           i=0;
           continue;
        }
        i++;
    }
    return mis;
}