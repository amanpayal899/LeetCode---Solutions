int minSubArrayLen(int target, int* nums, int numsSize) {
    int flag = 0;
    int min_len = INT_MAX;
    int i=0, j=0;
    int sum = 0;

    while(j<numsSize){
        sum += nums[j];
        while( i<= j & sum>=target){
        
            if((j-i) < min_len)
                min_len = j-i+1;
                flag = 1;
            sum -= nums[i];
            i++;
        }
        j++;
    }
    if (sum >= target){
        if(min_len>(j-i))
            min_len = j-i+1;
        flag=1;
    }
    if (flag){
        return min_len;
    }
    return 0;
}
