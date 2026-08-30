# Problem: Find Minimum in Rotated Sorted Array
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-12_130045 UTC
# URL: https://leetcode.com/submissions/detail/2030824431/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        small = float('+inf')
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] < small:
                small = nums[mid]
            if nums[low] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        return small