# Problem: Container With Most Water
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 13.9 MB
# Submitted: 2026-01-21_152714 UTC
# URL: https://leetcode.com/submissions/detail/1892283847/

int maxArea(int* height, int heightSize) {
   int small , maxwater=0;
   int i=0 , j= heightSize-1;
   while(i!=j){
    if(height[i] > height[j])
    small = j;
    else small = i;
    if(maxwater<height[small]*(j-i))
    maxwater=height[small]*(j-i);
    if(small==i) i++;
    else j--;

   }
   return maxwater ;
}