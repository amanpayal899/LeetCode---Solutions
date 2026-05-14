bool isGood(int* nums, int numsSize) {
    int max = nums[0];
    for( int i=1; i<numsSize; i++ ){
        if( nums[i] > max )
            max = nums[i];
    }
    int *result = (int*)calloc((max), sizeof(int));
    for( int i=0; i<numsSize; i++){
        result[nums[i]-1]++;
    }
    if(result[max-1] != 2)
        return false;
    for(int i=0; i<max-1; i++){
        if( result[i] !=1 )
            return false;
    }
    return true;
}
