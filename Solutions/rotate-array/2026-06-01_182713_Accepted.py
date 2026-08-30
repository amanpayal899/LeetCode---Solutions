# Problem: Rotate Array
# Status: Accepted
# Language: python3
# Runtime: 7 ms
# Memory: 26.5 MB
# Submitted: 2026-06-01_182713 UTC
# URL: https://leetcode.com/submissions/detail/2019448126/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverse(n-k, n-1)
        reverse(0, n-k-1)
        reverse(0, n-1)