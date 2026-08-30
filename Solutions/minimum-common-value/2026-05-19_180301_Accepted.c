# Problem: Minimum Common Value
# Status: Accepted
# Language: c
# Runtime: 123 ms
# Memory: 15 MB
# Submitted: 2026-05-19_180301 UTC
# URL: https://leetcode.com/submissions/detail/2007546628/

int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    for( int i=0; i<nums1Size; i++ ){
        for( int j=0; j<nums2Size && nums2[j]<=nums1[i]; j++ ){
            if( nums2[j] == nums1[i] )
                return nums2[j];
        }
    }
    return -1;
    
}