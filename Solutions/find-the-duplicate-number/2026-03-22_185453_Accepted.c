# Problem: Find the Duplicate Number
# Status: Accepted
# Language: c
# Runtime: 3 ms
# Memory: 17.4 MB
# Submitted: 2026-03-22_185453 UTC
# URL: https://leetcode.com/submissions/detail/1956063747/

int findDuplicate(int* nums, int numsSize) {
    int* check = (int*)calloc((numsSize-1),sizeof(int));
   for( int i=0 ; i<numsSize ; i++)
   {
    check[ nums[i]-1 ]++;
   }
   for( int i=0 ; i<numsSize-1; i++)
   {
    if( check[i]>1)
    return i+1;
   }
   return 0;
}