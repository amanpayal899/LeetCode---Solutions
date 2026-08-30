# Problem: Container With Most Water
# Status: Accepted
# Language: c
# Runtime: 2 ms
# Memory: 14.7 MB
# Submitted: 2026-03-02_191349 UTC
# URL: https://leetcode.com/submissions/detail/1936033870/

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