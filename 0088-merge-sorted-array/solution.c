void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    for(int i=m;i<(m+n);i++){
        nums1[i]=nums2[i-m];
    }
    int small=nums1[0];
    for(int i=0;i<(m+n);i++){
        for(int j=0;j<(m+n-i-1);j++){
            if(nums1[j]>nums1[j+1]){
                small=nums1[j+1];
                nums1[j+1]=nums1[j];
                nums1[j]=small;
            }
        }
    }
}
