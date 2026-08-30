# Problem: Single Number II
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 20.5 MB
# Submitted: 2026-04-27_133223 UTC
# URL: https://leetcode.com/submissions/detail/1989420158/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        # Look at every second element (0, 2, 4...)
        for i in range(0, len(nums) - 1, 3):
            if nums[i] != nums[i + 1]:
                return nums[i]
        
        # If we reached the end, the last element must be the single one
        return nums[-1]