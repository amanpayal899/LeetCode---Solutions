# Problem: Rotate Function
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-01_071037 UTC
# URL: https://leetcode.com/submissions/detail/1992365722/

int maxRotateFunction(int* nums, int numsSize) {
    int max=INT_MIN;
    for( int i=0; i<numsSize; i++ )
    {
        int temp_max = 0;
        for( int j=0; j<numsSize; j++)
        {
            int idx = (i+j) % numsSize;
            temp_max += j*nums[idx];
        }
        if( temp_max > max )
            max = temp_max;
    }
    return max;
}