# Problem: Toggle Light Bulbs
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-15_033259 UTC
# URL: https://leetcode.com/submissions/detail/1919630818/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdlib.h>
int* toggleLightBulbs(int* bulbs, int bulbsSize, int* returnSize) {
    int *arr = (int*)malloc(101*sizeof(int)) ;
    for(int i=0 ; i<bulbsSize ; i++){
        arr[i] = 0;
    }
    for(int i=0 ; i<bulbsSize ; i++){
        arr[bulbs[i]]++;
    }
    int j=0 ;
    for(int i=0 ; i<bulbsSize ; i++){
        if(arr[bulbs[i]]%2 != 0)
        {
            arr[j++]=bulbs[i];
            arr[bulbs[i]] = 0 ;
        }
    }
    *returnSize = j;
    int compare(const void *a, const void*b){
        return (*(int*)a - *(int*)b);
    }
    qsort(arr,j,sizeof(int),compare) ;
    return arr ;
}