# Problem: Find All Numbers Disappeared in an Array
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-29_153244 UTC
# URL: https://leetcode.com/submissions/detail/1901065420/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include<stdlib.h>
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
   int* arr=(int*)malloc((numsSize)*sizeof(int));
   int arr2[numsSize];
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
    *returnSize = j;
    return arr;
}