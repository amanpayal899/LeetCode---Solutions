# Problem: Check if Array Is Sorted and Rotated
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.7 MB
# Submitted: 2026-05-23_164021 UTC
# URL: https://leetcode.com/submissions/detail/2010983668/

bool check(int* nums, int numsSize) {
 int count = 0;
 for(int i=0; i<numsSize-1; i++){
    
    if(nums[i] <= nums[i+1]){
        continue;
    }
    else if((nums[i] > nums[i+1]) && count == 0){
        count++;
        continue;
    }
    else{
        return false;
    }
} 
if( (nums[0] < nums[numsSize-1]) && count > 0)
        return false;
return true;
}