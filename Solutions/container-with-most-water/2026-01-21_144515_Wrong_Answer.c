# Problem: Container With Most Water
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-21_144515 UTC
# URL: https://leetcode.com/submissions/detail/1892242134/

int maxArea(int* height, int heightSize) {
    int maxwater=height[0]*height[1];
    for(int i=0;i<heightSize;i++){
        int maxwater1=0 , j=i+1;
        while(j<heightSize){
            if(height[i] > height[j]){
                maxwater1=height[j]*(j-1);
            }
            if(maxwater < maxwater1){
                maxwater = maxwater1 ;
            }
            j++;
        }
    }
    return maxwater ;
}