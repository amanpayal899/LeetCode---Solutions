# Problem: Sum of Distances
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-23_134205 UTC
# URL: https://leetcode.com/submissions/detail/1986190066/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* distance(int* nums, int numsSize, int* returnSize) {
    long long *arr = (long long*) malloc(numsSize*sizeof(long long));
    *returnSize = numsSize;
    for( int i=0; i<numsSize; i++ )
    {
        long long sum=0;
        for( int j=0; j<numsSize; j++ )
        {
            if( nums[j]==nums[i] && j!=i )
            sum += i > j ? i-j : j-i;
        }
        arr[i] = sum;
    }
    return arr;
}