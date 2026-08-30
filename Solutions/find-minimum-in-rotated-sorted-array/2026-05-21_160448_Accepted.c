# Problem: Find Minimum in Rotated Sorted Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.1 MB
# Submitted: 2026-05-21_160448 UTC
# URL: https://leetcode.com/submissions/detail/2009180194/

int findMin(int* nums, int numsSize) {
    int small=nums[0];
    for( int i=numsSize-1; i>0; i--){
        if( nums[i] < small )
            small = nums[i];
        if( nums[i-1] > nums[i])
            return nums[i];
    }
    return small;
}