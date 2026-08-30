# Problem: Count Elements With Maximum Frequency
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-02_124912 UTC
# URL: https://leetcode.com/submissions/detail/1993329133/

int maxFrequencyElements(int* nums, int numsSize) {
    int freq[100] = {0};
    int max_freq = 0;
    for( int i=0; i<numsSize; i++ )
    {
        freq[ nums[i] ]++;
        if(freq[ nums[i] ]>max_freq)
        max_freq = freq[ nums[i] ];
    }
    int count=0;
    for( int i=0; i<100; i++ )
    {
        if( freq[i] == max_freq )
        count++;
    }
    return max_freq*count;
}