# Problem: Search Insert Position
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.4 MB
# Submitted: 2026-01-10_180713 UTC
# URL: https://leetcode.com/submissions/detail/1880998352/

int searchInsert(int* nums, int numsSize, int target) {int count=0;
    for(int i=0;i<numsSize;i++,count++){
        if(nums[i]==target)
        return i;
        else if(target<nums[i])
        return i;
    }
    return count;
}