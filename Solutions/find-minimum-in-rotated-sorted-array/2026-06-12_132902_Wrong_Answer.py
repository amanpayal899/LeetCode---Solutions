# Problem: Find Minimum in Rotated Sorted Array
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-12_132902 UTC
# URL: https://leetcode.com/submissions/detail/2030846895/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid - 1
        return nums[low]