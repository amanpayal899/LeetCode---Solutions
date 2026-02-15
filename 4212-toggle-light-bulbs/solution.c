/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdlib.h>
int* toggleLightBulbs(int* bulbs, int bulbsSize, int* returnSize) {
    int *arr = (int*)malloc(101*sizeof(int)) ;
    int count[101]={0};
    for(int i=0 ; i<bulbsSize ; i++){
        count[i] = 0;
    }
    for(int i=0 ; i<bulbsSize ; i++){
        count[bulbs[i]]++;
    }
    int j=0 ;
    for(int i=0 ; i<bulbsSize ; i++){
        if(count[bulbs[i]]%2 != 0)
        {
            arr[j++]=bulbs[i];
            count[bulbs[i]] = 0 ;
        }
    }
    *returnSize = j;
    int compare(const void *a, const void*b){
        return (*(int*)a - *(int*)b);
    }
    qsort(arr,j,sizeof(int),compare) ;
    return arr ;
}
