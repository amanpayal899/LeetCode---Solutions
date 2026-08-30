# Problem: Remove Duplicates from Sorted Array
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-01_190745 UTC
# URL: https://leetcode.com/submissions/detail/1904733036/

int removeDuplicates(int* nums, int numsSize) {
    
    char k = '#' ;int j= numsSize ;
    int result[j]={};
    j=0 ;
    for( int i=0; i<numsSize ; i++){
        if(k==nums[i])
            continue;
        k=nums[i];
        result[j++] = nums[i] ;
    }
    
    for(int i=0 ; i<numsSize ; i++){
        nums[i]=result[i];
    }
    return j;

}