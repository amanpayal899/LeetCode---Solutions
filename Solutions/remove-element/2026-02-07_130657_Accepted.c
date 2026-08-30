# Problem: Remove Element
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.8 MB
# Submitted: 2026-02-07_130657 UTC
# URL: https://leetcode.com/submissions/detail/1911285867/

int removeElement(int* nums, int numsSize, int val) {
    int count = 0 ;
    for( int i = 0 ; i < numsSize ; i++ ){
        if(nums[i] != val)
          nums[count++] = nums[i];
    }
    return count;
}
   