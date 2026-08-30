# Problem: First Missing Positive
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-03_050402 UTC
# URL: https://leetcode.com/submissions/detail/1936321587/

int firstMissingPositive(int* nums, int numsSize) {
    int mis = 1;
    for( int i = 0 ; i<numsSize ; i++ ){
        if( nums[i] == mis){
           mis++;
           i=0;
        }
    }
    return mis;
}