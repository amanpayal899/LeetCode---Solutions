/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* limitOccurrences(int* nums, int numsSize, int k, int* returnSize) {
    
    int max=nums[0];
    for(int i=0; i<numsSize; i++){
        if(nums[i]>max)
        max = nums[i];
    }
    int *result = (int*)malloc(numsSize*sizeof(int));
    int *feq = (int*) calloc(max, sizeof(int));
    for(int i=0; i<numsSize; i++){
        feq[nums[i]-1]++;
    }
    int j=0;
    for(int i=0; i<max; i++){
        if(feq[i]>=k){
        int temp=k;
            while(temp>0){
            result[j++] = i+1;
            temp--;
            }
        }
        else{
            int temp = feq[i];
            while(temp>0){
                result[j++] = i+1;
                temp--;
            }
        }
    }
    *returnSize = j;
    return result;

}
