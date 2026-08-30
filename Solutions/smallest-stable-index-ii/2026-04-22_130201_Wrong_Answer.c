# Problem: Smallest Stable Index II
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-22_130201 UTC
# URL: https://leetcode.com/submissions/detail/1985324633/

int firstStableIndex(int* nums, int numsSize, int k) {
    int min_array[numsSize];
    long max_array[numsSize];
    int min=nums[numsSize-1];
    int max=nums[0];
    for( int i=numsSize-1, j=0; i>=0 || j<numsSize; i--, j++ )
    {
        if( nums[i]<min )
        min = nums[i];
        min_array[i] = min;
        if( nums[j] > max )
        max = nums[j];
        max_array[j] = max;

        if( max_array[j] - min_array[i] <= k )
        return i;
    }
    return -1;
    
}