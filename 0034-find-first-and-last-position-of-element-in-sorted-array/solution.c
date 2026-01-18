/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int* pos=(int*)malloc(2*sizeof(int));
    pos[0]=-1; pos[1]=-1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==target){
            if(pos[0]==-1){
            pos[0]=i;pos[1]=i;
            }
            else pos[1]=i;
        }
    }
    *returnSize =2;
    return pos;
    
}
