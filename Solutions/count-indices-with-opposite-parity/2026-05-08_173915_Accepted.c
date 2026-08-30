# Problem: Count Indices With Opposite Parity
# Status: Accepted
# Language: c
# Runtime: 4 ms
# Memory: 13.4 MB
# Submitted: 2026-05-08_173915 UTC
# URL: https://leetcode.com/submissions/detail/1998316423/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countOppositeParity(int* nums, int numsSize, int* returnSize) {
    int* answer = (int*) malloc( numsSize*sizeof(int));
    for( int i=0; i<numsSize; i++ )
    {
        int even = nums[i]%2;
        int count=0;
        for( int j=i+1; j<numsSize; j++ )
        {
            if( nums[j]%2 != even )
                count++;
           
        }
        answer[i] = count;
    }
    *returnSize = numsSize;
    return answer;
}