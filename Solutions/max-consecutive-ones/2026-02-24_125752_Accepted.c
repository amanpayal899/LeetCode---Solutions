# Problem: Max Consecutive Ones
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 12.5 MB
# Submitted: 2026-02-24_125752 UTC
# URL: https://leetcode.com/submissions/detail/1929643157/

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int count = 0 ;
    int max = 0 ;
    for( int i = 0 ; i < numsSize ; i++){
        if( nums[i] == 1 )
          count ++;
        else if( nums[i] == 0 )
          count = 0;
        if( count > max )
          max = count ;
    }
    return max;
}