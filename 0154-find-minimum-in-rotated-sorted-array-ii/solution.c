int findMin(int* nums, int numsSize) {
    for( int i=numsSize-1; i>0; i-- ){
        if( (nums[i-1] > nums[i]) )
            return nums[i];
    }
    return nums[0];
}
