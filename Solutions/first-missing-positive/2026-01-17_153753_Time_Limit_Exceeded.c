# Problem: First Missing Positive
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-17_153753 UTC
# URL: https://leetcode.com/submissions/detail/1887952984/

int firstMissingPositive(int* nums, int numsSize) {
   int k=1;
   while(1){
    int m=0;
   for(int i=0;i<numsSize;i++){
     if(nums[i]==k){
        m++;k++;break;
     }
   }
   if(m==0) return k;
   }
   return 1;
}