# Problem: Intersection of Two Arrays
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-18_232415 UTC
# URL: https://leetcode.com/submissions/detail/1923785513/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int *result = (int*)malloc(nums2Size*sizeof(int)) ;
    int e=0;
    for( int i=0,j=0 ; j<nums2Size ; ){
        if(nums2[j]==nums1[i]){
            result[e] = nums2[j];
            i=0;e++;j++;
            continue;
        }
        if(i==nums1Size-1){
            i=0;
            continue;
        }
        i++;
        
    }
   *returnSize = e ;
    return result ;
}