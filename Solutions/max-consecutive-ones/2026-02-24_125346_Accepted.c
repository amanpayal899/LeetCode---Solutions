# Problem: Max Consecutive Ones
# Status: Accepted
# Language: c
# Runtime: 4 ms
# Memory: 12.7 MB
# Submitted: 2026-02-24_125346 UTC
# URL: https://leetcode.com/submissions/detail/1929639746/

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int max=0,temp=0;
    for(int i=0 ; i<numsSize ; i++){
        if( nums[i] == 1 ){
            temp++;
            if( temp > max ) 
            max = temp ;
        }
        else {
            temp = 0;
        }
    }
    return max;
}