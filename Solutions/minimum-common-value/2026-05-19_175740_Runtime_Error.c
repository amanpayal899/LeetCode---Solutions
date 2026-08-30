# Problem: Minimum Common Value
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-19_175740 UTC
# URL: https://leetcode.com/submissions/detail/2007541009/

int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    for( int i=0; i<nums1Size; i++ ){
        for( int j=0; nums2[j]<=nums1[i]; j++ ){
            if( nums2[j] == nums1[i] )
                return nums2[j];
        }
    }
    return -1;
    
}