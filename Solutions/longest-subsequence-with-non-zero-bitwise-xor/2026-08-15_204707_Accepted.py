# Problem: Longest Subsequence With Non-Zero Bitwise XOR
# Status: Accepted
# Language: python3
# Runtime: 42 ms
# Memory: 32.9 MB
# Submitted: 2026-08-15_204707 UTC
# URL: https://leetcode.com/submissions/detail/2108243659/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        all_zero = 1
        result = 0
        for i in nums:
            if i!=0:
                all_zero = 0
            result ^= i
        if result:
            return n
        if all_zero == 1:
            return 0
        return n-1
