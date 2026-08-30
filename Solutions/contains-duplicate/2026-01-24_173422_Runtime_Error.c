# Problem: Contains Duplicate
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-24_173422 UTC
# URL: https://leetcode.com/submissions/detail/1895590565/

bool containsDuplicate(int* nums, int numsSize) {
   int arr[numsSize];
   int i=0;
   for(;i<numsSize;i++){
       arr[i]=nums[i];
   } 
   for(i=1;i<numsSize;i++){
      int small=arr[i];
      for(int j =i+1;j<numsSize;j++){
       if(small>arr[j])
       small=arr[j]; 
      }
      arr[i]=small;
   }
   for(i=0;i<numsSize;i++){
    if(arr[i]==arr[i+1])
    return 1;break;
   }
   return 0;
}