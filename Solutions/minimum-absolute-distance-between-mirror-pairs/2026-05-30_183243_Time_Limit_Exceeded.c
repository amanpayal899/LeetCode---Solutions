# Problem: Minimum Absolute Distance Between Mirror Pairs
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-30_183243 UTC
# URL: https://leetcode.com/submissions/detail/2017504621/

int rev(int num,int rev){
    while(num>0){
            rev = rev*10 + num%10;
            num /= 10;
        }
    return rev;
}
int minMirrorPairDistance(int* nums, int numsSize) {
    int min_dis=-1;
    for(int i=0; i<numsSize-1; i++){
        int current=nums[i];
        int rev_num=0;
        rev_num = rev(nums[i], 0);
        for(int j=i+1; j<numsSize; j++){
            if( rev_num == nums[j] ){
                int temp = j-i;
                if( min_dis==-1 || min_dis>temp ){
                min_dis = temp;
                }
            }
        }
    }
    return min_dis;
}