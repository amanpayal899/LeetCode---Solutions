int minimumPrefixLength(int* nums, int numsSize) {
  int count =1;
    for(int i=numsSize-1 ; i>=1 ; i--){
        if(nums[i]>nums[i-1])
            count++;
        else if(nums[i]<=nums[i-1])
            break;
    }
    count=numsSize-count;
    return count;
}
