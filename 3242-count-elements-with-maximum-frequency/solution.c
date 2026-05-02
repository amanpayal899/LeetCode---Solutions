int maxFrequencyElements(int* nums, int numsSize) {
    int freq[101] = {0};
    int max = 0;
    for( int i=0; i<numsSize; i++ )
    {
        freq[ nums[i] ]++;
        if( max < freq[ nums[i] ])
            max = freq[nums[i]];
    }
    int count=0;
    for( int i=0; i<101; i++ )
    {
        if( freq[i] == max )
            count++;
    }
    return max*count;
}
