class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int n = nums.size();
        if (n==0){
            return 0;
        }
        int result = nums[0];
        int flag = 0;
        for(int i=1; i<n; i++){
            result ^= nums[i];
            if(nums[i]!=0){
                flag = 1;
            }
        }
        if (result){
            return n;
        }
        if (flag){
            return n-1;
        }
        return 0;
        
    }
};
