# Problem: Find All Numbers Disappeared in an Array
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 36.6 MB
# Submitted: 2026-01-29_160048 UTC
# URL: https://leetcode.com/submissions/detail/1901095520/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include<stdlib.h>
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
   int* arr=(int*)malloc((numsSize)*sizeof(int));
   int* arr2= (int*) calloc(numsSize,sizeof(int));
    for(int i = 0 ; i<numsSize ; i++){
       arr2[nums[i]-1] = -1;

    }
    int j=0;
    for( int i = 0 ; i<numsSize ; i++){
        if(arr2[i] != -1 ){
            arr[j] = i+1 ;
            j++;
        }
    }
    free(arr2);
    *returnSize = j;
    return arr;
}