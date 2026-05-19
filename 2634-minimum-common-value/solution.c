int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    for( int i=0; i<nums1Size; i++ ){
        for( int j=0; j<nums2Size && nums2[j]<=nums1[i]; j++ ){
            if( nums2[j] == nums1[i] )
                return nums2[j];
        }
    }
    return -1;
    
}
