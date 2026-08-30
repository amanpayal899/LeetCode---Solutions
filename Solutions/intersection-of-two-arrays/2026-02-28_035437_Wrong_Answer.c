# Problem: Intersection of Two Arrays
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-28_035437 UTC
# URL: https://leetcode.com/submissions/detail/1933247283/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
  int *result = (int*)malloc((nums1Size+nums2Size)*sizeof(int)) ;
  int *temp = (int*)calloc(1001,sizeof(int)) ;
  int intrsec = 0;
  for( int i=0 ; i<nums1Size ; i++){
    for( int j=0 ; j<nums2Size ; j++){
        if( nums1[i] == nums2[j] ){
            temp[nums1[i]] = nums1[i];
            break;
        }
    }
  }
  for( int i=0 ; i<1001 ; i++){
    if( temp[i] != 0)
      result[ intrsec++ ] = temp[i] ;
  }
  *returnSize = intrsec ;
  return result;
}