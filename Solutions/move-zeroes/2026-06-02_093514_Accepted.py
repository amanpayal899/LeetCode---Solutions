# Problem: Move Zeroes
# Status: Accepted
# Language: python3
# Runtime: 5 ms
# Memory: 20.4 MB
# Submitted: 2026-06-02_093514 UTC
# URL: https://leetcode.com/submissions/detail/2020018466/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(0, n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1