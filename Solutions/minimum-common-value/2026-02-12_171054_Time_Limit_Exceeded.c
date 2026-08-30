# Problem: Minimum Common Value
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-12_171054 UTC
# URL: https://leetcode.com/submissions/detail/1917207466/

int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0 ;
    for( int j=0 ; i<nums1Size ; j++){
         if(nums2[j]==nums1[i])
         return nums1[i];
         else if(j==nums2Size-1){
            i++;
            j=-1;
        }
    }
    
      return -1;
    
}