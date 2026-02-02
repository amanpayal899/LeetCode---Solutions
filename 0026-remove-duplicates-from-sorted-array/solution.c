int removeDuplicates(int* nums, int numsSize) {
    int i=0;
    for(int j=1 ; j<numsSize ; ){
       if(nums[i] == nums[j]){
        j++;
       }
       else{
        nums[++i]=nums[j++];
       }
    } 
    return i+1;
}
