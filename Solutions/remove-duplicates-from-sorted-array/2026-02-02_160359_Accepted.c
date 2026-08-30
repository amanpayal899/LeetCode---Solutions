# Problem: Remove Duplicates from Sorted Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 12.3 MB
# Submitted: 2026-02-02_160359 UTC
# URL: https://leetcode.com/submissions/detail/1905645375/

int removeDuplicates(int* nums, int numsSize) {
    int i=0;
    for(int j=1 ; j<numsSize ; ){
       if(nums[i] == nums[j]){
        j++;
       }
       else{
        nums[++i]=nums[j++];
       }
    } 
    return i+1;
}