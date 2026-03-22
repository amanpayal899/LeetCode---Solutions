int findDuplicate(int* nums, int numsSize) {
    int* check = (int*)calloc((numsSize-1),sizeof(int));
   for( int i=0 ; i<numsSize ; i++)
   {
    check[ nums[i]-1 ]++;
   }
   for( int i=0 ; i<numsSize-1; i++)
   {
    if( check[i]>1)
    return i+1;
   }
   return 0;
}
