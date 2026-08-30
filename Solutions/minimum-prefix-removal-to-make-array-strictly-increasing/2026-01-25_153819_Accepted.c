# Problem: Minimum Prefix Removal to Make Array Strictly Increasing
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 21.8 MB
# Submitted: 2026-01-25_153819 UTC
# URL: https://leetcode.com/submissions/detail/1896636125/

int minimumPrefixLength(int* nums, int numsSize) {
  int count =1;
    for(int i=numsSize-1 ; i>=1 ; i--){
        if(nums[i]>nums[i-1])
            count++;
        else if(nums[i]<=nums[i-1])
            break;
    }
    count=numsSize-count;
    return count;
}