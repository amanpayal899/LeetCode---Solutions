int missingNumber(int* nums, int numsSize) {
    int sum1 = 0,sum2 = 0;
    for(int i = 0 ; i<numsSize ; i++){
        sum1 += i+1 ;
        sum2 += nums[i] ;
    }
    return sum1-sum2 ;
    
}
