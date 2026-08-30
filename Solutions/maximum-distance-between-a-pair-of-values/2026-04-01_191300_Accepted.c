# Problem: Maximum Distance Between a Pair of Values
# Status: Accepted
# Language: c
# Runtime: 21 ms
# Memory: 17.1 MB
# Submitted: 2026-04-01_191300 UTC
# URL: https://leetcode.com/submissions/detail/1966200441/

int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int max_dis=0;
    for( int i=0; i<nums1Size; i++ )
    {
        int start=i, end=nums2Size-1;
        while(start<=end)
        {
            int mid = ((end-start)/2)+start;
            if( nums2[mid]<nums1[i] )
            {
                end=mid-1;
            }
            else if( nums2[mid]>=nums1[i])
            {
               if(max_dis<mid-i) 
               {
                    max_dis=mid-i;
               }
               start=mid+1;
            }
        }
    }
    return max_dis;
}