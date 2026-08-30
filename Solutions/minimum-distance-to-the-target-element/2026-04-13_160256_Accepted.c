# Problem: Minimum Distance to the Target Element
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9 MB
# Submitted: 2026-04-13_160256 UTC
# URL: https://leetcode.com/submissions/detail/1977477773/

int getMinDistance(int* nums, int numsSize, int target, int start) {
    int min=numsSize, temp_min=numsSize;
    for( int i=0; i<numsSize; i++ ){
        if( nums[i]==target ){
            temp_min = i-start;
            if( temp_min<0 ){
                temp_min *= -1;
            }
        }
        if( temp_min<min )
        min = temp_min;
    }
    return min;
}