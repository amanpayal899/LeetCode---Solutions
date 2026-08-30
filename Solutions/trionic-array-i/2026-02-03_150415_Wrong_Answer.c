# Problem: Trionic Array I
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-03_150415 UTC
# URL: https://leetcode.com/submissions/detail/1906840702/

bool isTrionic(int* nums, int numsSize) {
    int count = 0 ;
    for(int i =0 ; i<numsSize-1 ; i++){
        if(nums[i] == nums[i+1])
        return false ;

        else if(nums[i] < nums[i+1]){
             if(count == 0 || count ==2)
             count++;
            }
        else if ( nums[i+1] <nums[i]){
            if(count == 1)
            count ++;
        }
    }
    if(count == 3)
    return true ;
    return NULL ;
}