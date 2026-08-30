# Problem: Concatenation of Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-05-07_184834 UTC
# URL: https://leetcode.com/submissions/detail/1997640421/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        ans = ans + nums
        return ans