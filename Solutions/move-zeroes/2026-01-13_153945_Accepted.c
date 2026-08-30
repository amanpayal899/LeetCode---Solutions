# Problem: Move Zeroes
# Status: Accepted
# Language: c
# Runtime: 450 ms
# Memory: 19.6 MB
# Submitted: 2026-01-13_153945 UTC
# URL: https://leetcode.com/submissions/detail/1883954651/

void moveZeroes(int* nums, int numsSize) {
    for(int i=0;i<numsSize;i++){
        for(int j=0;j<numsSize-i-1;j++){
            if(nums[j]==0){
               nums[j]=nums[j+1];
               nums[j+1]=0;
            }
        }
    }
}