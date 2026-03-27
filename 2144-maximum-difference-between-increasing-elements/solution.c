int maximumDifference(int* nums, int numsSize) {
   int max_diff = 0, min=nums[0];
   if( numsSize <= 1)
     return -1;
    for( int i=0 ; i<numsSize ; i++ )
    {
        if( nums[i] < min)
        min = nums[i];
        else if( nums[i]-min >= max_diff)
        max_diff = nums[i]-min;
    }
    if( max_diff < 1)
    return -1;
    return max_diff;
}
