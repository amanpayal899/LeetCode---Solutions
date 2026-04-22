int firstStableIndex(int* nums, int numsSize, int k) {
    int min_array[numsSize];
    long max_array[numsSize];
    int min=nums[numsSize-1];
    int max=nums[0];
    for( int i=numsSize-1, j=0; i>=0 || j<numsSize; i--, j++ )
    {
        if( nums[i]<min )
        min = nums[i];
        min_array[i] = min;
        if( nums[j] > max )
        max = nums[j];
        max_array[j] = max;
    }
    for( int i=0; i<numsSize; i++ )
    {
        if( max_array[i] - min_array[i] <= k )
        return i;
    }
    return -1;
    
}
