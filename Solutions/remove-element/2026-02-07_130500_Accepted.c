# Problem: Remove Element
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.7 MB
# Submitted: 2026-02-07_130500 UTC
# URL: https://leetcode.com/submissions/detail/1911284301/

int removeElement(int* nums, int numsSize, int val) {
    long count = 0 ;
    for( long i = 0 ; i < numsSize ; i++ ){
        if(nums[i] != val)
          nums[count++] = nums[i];
    }
    return count;
}
   