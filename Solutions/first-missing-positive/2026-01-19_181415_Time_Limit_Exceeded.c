# Problem: First Missing Positive
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-19_181415 UTC
# URL: https://leetcode.com/submissions/detail/1890219486/

int firstMissingPositive(int* nums, int numsSize) {
    for(int i=0,j=1;i<numsSize;i++){
        if(nums[i]==j){
            j++;i=-1;continue;
        }
        else if(i==numsSize-1)
        return j;
 }
 return 0;
}