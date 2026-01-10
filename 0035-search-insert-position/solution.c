int searchInsert(int* nums, int numsSize, int target) {int count=0;
    for(int i=0;i<numsSize;i++,count++){
        if(nums[i]==target)
        return i;
        else if(target<nums[i])
        return i;
    }
    return count;
}
