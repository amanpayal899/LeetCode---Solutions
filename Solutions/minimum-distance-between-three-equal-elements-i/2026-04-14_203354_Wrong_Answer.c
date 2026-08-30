# Problem: Minimum Distance Between Three Equal Elements I
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-14_203354 UTC
# URL: https://leetcode.com/submissions/detail/1978650641/

int minimumDistance(int* nums, int numsSize) {
    int distance=numsSize;
    for( int i=0; i<numsSize; i++ ){
        int count=1;
        int temp_dis=0;
        for( int j=i+1; j<numsSize; j++ ){
            if( nums[i]==nums[j] ){
                if(count=3)
                break;
                count++;
                temp_dis=temp_dis+i-j;
            }
            if( temp_dis < distance )
            distance=temp_dis;
        }
    }
    return distance;
}