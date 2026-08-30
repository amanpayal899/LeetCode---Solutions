# Problem: Count Elements With Maximum Frequency
# Status: Accepted
# Language: c
# Runtime: 1 ms
# Memory: 9.9 MB
# Submitted: 2026-05-02_132939 UTC
# URL: https://leetcode.com/submissions/detail/1993353658/

int maxFrequencyElements(int* nums, int numsSize) {
    int freq[101] = {0};
    int max = 0;
    for( int i=0; i<numsSize; i++ )
    {
        freq[ nums[i] ]++;
        if( max < freq[ nums[i] ])
            max = freq[nums[i]];
    }
    int count=0;
    for( int i=0; i<101; i++ )
    {
        if( freq[i] == max )
            count++;
    }
    return max*count;
}