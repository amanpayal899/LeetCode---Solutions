# Problem: Longest Subsequence With Non-Zero Bitwise XOR
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-15_203820 UTC
# URL: https://leetcode.com/submissions/detail/2108238907/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        seq_len = 1
        seq_xor = nums[0]
        prev_len = 1
        for i in range(1,n):
            if (seq_xor ^ nums[i]) == 0:
                if seq_xor != 0:
                    prev_len = seq_len
                seq_xor ^= nums[i]
                seq_len+=1
            else:
            
                seq_xor ^= nums[i]
                seq_len += 1

        if seq_xor:
            return seq_len
        return prev_len