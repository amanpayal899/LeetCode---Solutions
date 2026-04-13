int getMinDistance(int* nums, int numsSize, int target, int start) {
    int min=numsSize, temp_min=numsSize;
    for( int i=0; i<numsSize; i++ ){
        if( nums[i]==target ){
            temp_min = i-start;
            if( temp_min<0 ){
                temp_min *= -1;
            }
        }
        if( temp_min<min )
        min = temp_min;
    }
    return min;
}
