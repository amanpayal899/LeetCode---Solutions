/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
   int *ans = (int*)malloc(2*numsSize*sizeof(int));
   *returnSize=2*numsSize;
   int i=0;
   for(;i+numsSize<2*numsSize;i++){
      ans[i]=nums[i];
      ans[i+numsSize]=nums[i];
   } 
   return ans;
}
