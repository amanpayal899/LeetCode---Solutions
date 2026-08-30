# Problem: Contains Duplicate
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 31.3 MB
# Submitted: 2026-03-09_194730 UTC
# URL: https://leetcode.com/submissions/detail/1943270036/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)