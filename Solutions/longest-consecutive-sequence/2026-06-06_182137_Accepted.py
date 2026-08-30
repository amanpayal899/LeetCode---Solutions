# Problem: Longest Consecutive Sequence
# Status: Accepted
# Language: python3
# Runtime: 46 ms
# Memory: 36.6 MB
# Submitted: 2026-06-06_182137 UTC
# URL: https://leetcode.com/submissions/detail/2024645533/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for i in my_set:
            if i-1 not in my_set:
                current_sequence_count = 1
                x = 1
                while i + x in my_set:
                    current_sequence_count += 1
                    x += 1
                if current_sequence_count > longest:
                    longest = current_sequence_count
                
        return longest
