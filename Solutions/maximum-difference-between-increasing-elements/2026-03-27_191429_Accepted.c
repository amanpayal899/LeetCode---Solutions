# Problem: Maximum Difference Between Increasing Elements
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.1 MB
# Submitted: 2026-03-27_191429 UTC
# URL: https://leetcode.com/submissions/detail/1961216826/

int maximumDifference(int* nums, int numsSize) {
   int max_diff = 0, min=nums[0];
   if( numsSize <= 1)
     return -1;
    for( int i=0 ; i<numsSize ; i++ )
    {
        if( nums[i] < min)
        min = nums[i];
        else if( nums[i]-min >= max_diff)
        max_diff = nums[i]-min;
    }
    if( max_diff < 1)
    return -1;
    return max_diff;
}