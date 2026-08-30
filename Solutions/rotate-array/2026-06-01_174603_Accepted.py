# Problem: Rotate Array
# Status: Accepted
# Language: python3
# Runtime: 1735 ms
# Memory: 26.5 MB
# Submitted: 2026-06-01_174603 UTC
# URL: https://leetcode.com/submissions/detail/2019401258/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(0, k):
            temp = nums.pop()
            nums.insert(0, temp)