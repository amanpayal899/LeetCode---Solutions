# Problem: Trionic Array I
# Status: Accepted
# Language: c
# Runtime: 1 ms
# Memory: 8.6 MB
# Submitted: 2026-02-03_162608 UTC
# URL: https://leetcode.com/submissions/detail/1906946356/

bool isTrionic(int* nums, int numsSize) {
    int count = 0 ;int i =0 , j=0 ;
    for( ; i<numsSize-1 ; i++){

        if(nums[i] == nums[i+1])
        return false ;

        else if(nums[i] < nums[i+1]){
             if(count ==3 || count ==0)
             count+=2;
            }
        else if ( (nums[i+1] <nums[i])){
            if(i==0) break;
            if(count == 2 || count == 5 ){
            count ++;
            }
        }
        
    }
    if(count == 5)
    return true ;
    return NULL ;
}