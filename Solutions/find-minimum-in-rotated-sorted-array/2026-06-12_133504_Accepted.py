# Problem: Find Minimum in Rotated Sorted Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-06-12_133504 UTC
# URL: https://leetcode.com/submissions/detail/2030851531/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid
        return nums[low]