# Problem: Find the Score Difference in a Game
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 10.3 MB
# Submitted: 2026-02-22_025905 UTC
# URL: https://leetcode.com/submissions/detail/1926902539/

int scoreDifference(int* nums, int numsSize) {
    int p1=0,p2=0;
    int *active = &p1;
    for( int i=0 ; i<numsSize ; i++){
        if( nums[i]%2 == 1 ){
           if(active == &p1)
             active = &p2;
            else active = &p1;
        }
        if((i+1)%6 == 0){
            if(active == &p1)
             active = &p2;
            else active = &p1;
        }
        *active += nums[i];
    }
    return p1-p2;
}