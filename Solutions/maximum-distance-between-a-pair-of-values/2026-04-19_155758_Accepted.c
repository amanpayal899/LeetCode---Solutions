# Problem: Maximum Distance Between a Pair of Values
# Status: Accepted
# Language: c
# Runtime: 30 ms
# Memory: 17 MB
# Submitted: 2026-04-19_155758 UTC
# URL: https://leetcode.com/submissions/detail/1982799853/

int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int max_distance = 0;
    for( int i=0; i<nums1Size; i++ )
    {
        for( int start=0, end=nums2Size-1; start<=end; )
        {
            int mid = (end-start)/2 + start;
            if( nums2[mid] >= nums1[i] )
            {
                if(mid-i >= max_distance)
                max_distance = mid-i;
                start = mid+1;
            }
            else 
            {
                end = mid-1;
            }
        }
    }
    return max_distance;
}