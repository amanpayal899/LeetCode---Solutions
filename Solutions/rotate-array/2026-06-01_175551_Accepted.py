# Problem: Rotate Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 26.4 MB
# Submitted: 2026-06-01_175551 UTC
# URL: https://leetcode.com/submissions/detail/2019412510/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]