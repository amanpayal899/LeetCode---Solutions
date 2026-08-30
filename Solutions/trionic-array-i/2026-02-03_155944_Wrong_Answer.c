# Problem: Trionic Array I
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-03_155944 UTC
# URL: https://leetcode.com/submissions/detail/1906909737/

bool isTrionic(int* nums, int numsSize) {
    int count = 0 ;int i =0 ;
    for( ; i<numsSize-1 ; i++){
        if(nums[i] == nums[i+1])
        return false ;

        else if(nums[i] < nums[i+1]){
             if(count ==2 || count == 0)
             count++;
            }
        else if ( nums[i+1] <nums[i]){
            if(count == 1)
            count ++;
            else if(i==0) break;
        }
        
    }
    if(count == 3)
    return true ;
    return NULL ;
}