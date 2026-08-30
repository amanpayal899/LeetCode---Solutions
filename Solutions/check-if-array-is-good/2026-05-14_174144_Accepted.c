# Problem: Check if Array is Good
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.5 MB
# Submitted: 2026-05-14_174144 UTC
# URL: https://leetcode.com/submissions/detail/2003196935/

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