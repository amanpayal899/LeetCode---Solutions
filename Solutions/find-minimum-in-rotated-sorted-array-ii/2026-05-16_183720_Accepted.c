# Problem: Find Minimum in Rotated Sorted Array II
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9 MB
# Submitted: 2026-05-16_183720 UTC
# URL: https://leetcode.com/submissions/detail/2004854868/

int findMin(int* nums, int numsSize) {
    for( int i=numsSize-1; i>0; i-- ){
        if( (nums[i-1] > nums[i]) )
            return nums[i];
    }
    return nums[0];
}