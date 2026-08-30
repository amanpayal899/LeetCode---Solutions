# Problem: Majority Element
# Status: Accepted
# Language: python3
# Runtime: 2 ms
# Memory: 21.3 MB
# Submitted: 2026-08-17_195638 UTC
# URL: https://leetcode.com/submissions/detail/2110637038/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]