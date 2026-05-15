int findMin(int* nums, int numsSize) {
    int small=nums[0];
    for( int i=numsSize-1; i>0; i--){
        if( nums[i] < small )
            small = nums[i];
        if( nums[i-1] > nums[i])
            return nums[i];
    }
    return small;
}
