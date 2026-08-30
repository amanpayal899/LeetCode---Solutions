# Problem: Find Minimum in Rotated Sorted Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Submitted: 2026-06-12_132019 UTC
# URL: https://leetcode.com/submissions/detail/2030839932/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        small = float('+inf')
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] < small:
                small = nums[mid]
            if nums[mid] >= nums[low]:
                if small > nums[low]:
                    small = nums[low]
                low = mid + 1
            else:
                high = mid - 1
        return small