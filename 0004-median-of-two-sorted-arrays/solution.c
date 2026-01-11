double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int m=nums1Size,n=nums2Size;
    int nums3[m+n];
    int i=0;
    for(;i<m;i++){
        nums3[i]=nums1[i];
    }
    for(int j=0;i<(m+n);i++,j++){
        nums3[i]=nums2[j];
    }
    int temp;
    for(int j=0;j<(m+n);j++){
         for(i=0;i<(m+n-j-1);i++){
             if(nums3[i]>nums3[i+1]){
             temp=nums3[i];
             nums3[i]=nums3[i+1];
             nums3[i+1]=temp;
            }
        }
    }
    if((m+n)%2==0)
    return ( nums3[((m+n)/2)-1]+nums3[((m+n)/2)] )/2.00;
    return nums3[((m+n+1)/2)-1];

}
