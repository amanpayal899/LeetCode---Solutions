int missingNumber(int* nums, int numsSize) {
    int expected_sum;
    expected_sum = (numsSize*(numsSize+1))/2;
    int arr_sum = 0;
    for(int i=0; i<numsSize; i++){
        arr_sum += nums[i];
    }
    return ( expected_sum - arr_sum);
}
