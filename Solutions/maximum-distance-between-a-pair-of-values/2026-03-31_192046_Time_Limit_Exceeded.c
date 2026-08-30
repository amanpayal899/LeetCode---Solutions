# Problem: Maximum Distance Between a Pair of Values
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-31_192046 UTC
# URL: https://leetcode.com/submissions/detail/1965235911/

int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int max_dis=0;
    for(int i=0; i<nums1Size; i++)
    {
        for(int j=nums2Size-1; j>=i; j--)
        {
            if( (nums1[i]<=nums2[j]) && (j-i>=max_dis))
            {
                max_dis = j-i;
            }

        }
    }
    return max_dis;
}