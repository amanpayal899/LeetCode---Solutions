int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
 for(int i=0 ; i<nums1Size ; i++){
    int strt=0,end=nums2Size-1 ;
    while( strt<=end){
        int mid = strt+(end-strt)/2 ;
        if(nums2[mid] == nums1[i])
           return nums2[mid] ;
        else if(nums1[i] < nums2[mid]){
            end = mid-1;
        }
        else if(nums1[i] > nums2[mid])
            strt = mid+1;
    }
 
}
return -1;
}
