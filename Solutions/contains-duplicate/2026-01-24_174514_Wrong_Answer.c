# Problem: Contains Duplicate
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-24_174514 UTC
# URL: https://leetcode.com/submissions/detail/1895602607/

bool containsDuplicate(int* nums, int numsSize) {
   int arr[numsSize];
   int i=0;
   for(;i<numsSize;i++){
       arr[i]=nums[i];
   } 
   for(i=0;i<numsSize && numsSize !=1 ;i++){
      int small=arr[i];
      for(int j =i+1;j<numsSize;j++){
       if(small>arr[j])
       small=arr[j]; 
      }
      arr[i]=small;
   }
   for(i=0;i<numsSize-1 && numsSize !=1 ;i++){
    if(arr[i]==arr[i+1])
    return 1;
   }
   return 0;
}