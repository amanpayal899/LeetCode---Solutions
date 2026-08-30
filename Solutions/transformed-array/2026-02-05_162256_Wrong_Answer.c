# Problem: Transformed Array
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-05_162256 UTC
# URL: https://leetcode.com/submissions/detail/1909323877/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructTransformedArray(int* nums, int numsSize, int* returnSize) {
  int *result = (int *)malloc(numsSize * sizeof(int)) ;
  *returnSize = numsSize ;
  for ( int i = 0 , j=0 ; i<numsSize ; i++ ) {
    j = nums[i] ;
    if(nums[i] == 0)
    result[i] = 0 ;
    else if ( nums[i] + i > numsSize - 1 ){
        
        j+= i ;
        j%= numsSize ;
        result[i] = nums[j] ;
    }
    else if( nums[i] < 0 && (nums[i] + i )< 0){
        j = -nums[i] ;
        j-= i ;
        j%= numsSize ;
        if(j==0)
        result[i] = nums[ numsSize -1] ;
        else result[i] = nums[ numsSize - j ] ;

    }
    else if ( nums[i] > 0) {
        result[i] = nums[ nums[i] + i] ;
    }
    else if ( nums[i] < 0) {
        result[i] = nums[ nums[i] + i] ;
    }
  }
  return result ;

}