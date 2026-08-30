# Problem: Longest Subsequence With Non-Zero Bitwise XOR
# Status: Accepted
# Language: cpp
# Runtime: 0 ms
# Memory: 171.3 MB
# Submitted: 2026-08-16_183751 UTC
# URL: https://leetcode.com/submissions/detail/2109378458/

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