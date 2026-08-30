# Problem: Minimum Common Value
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-14_151108 UTC
# URL: https://leetcode.com/submissions/detail/1919084886/

int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
 for(int i=0 ; i<nums1Size ; i++){
    int strt=nums2[0],end=nums2[nums2Size-1] ;
    while( strt<=end){
        int mid = strt+(end-strt)/2 ;
        if(mid == nums1[i])
           return mid ;
        else if(nums1[i] < mid){
            end = mid-1;
        }
        else if(nums1[i] > mid)
            strt = mid+1;
    }
 
}
return -1;
}