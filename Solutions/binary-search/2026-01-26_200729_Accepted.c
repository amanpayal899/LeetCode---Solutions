# Problem: Binary Search
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.6 MB
# Submitted: 2026-01-26_200729 UTC
# URL: https://leetcode.com/submissions/detail/1898042187/

int search(int* nums, int numsSize, int target) {
     int high=numsSize-1;
     int low=0;
     while(low<=high){
        int mid=low+(high-low)/2;
        if(nums[mid]==target)
        return mid;
        else if(nums[mid]>target){
            high=mid-1;
        }
        else if(nums[mid]<target)
        low=mid+1;
     }
     return -1; 
}