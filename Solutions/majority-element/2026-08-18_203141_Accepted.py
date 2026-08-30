# Problem: Majority Element
# Status: Accepted
# Language: python3
# Runtime: 15 ms
# Memory: 21.4 MB
# Submitted: 2026-08-18_203141 UTC
# URL: https://leetcode.com/submissions/detail/2111980466/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > n//2:
                return i
        return 0