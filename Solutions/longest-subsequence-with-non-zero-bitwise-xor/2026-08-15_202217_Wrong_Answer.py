# Problem: Longest Subsequence With Non-Zero Bitwise XOR
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-15_202217 UTC
# URL: https://leetcode.com/submissions/detail/2108229442/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        seq_len = 0
        seq_xor = 0
        for i in nums:
            if (seq_xor ^ i) == 0:
                continue
            else:
                seq_xor ^= i
                seq_len += 1

        return seq_len