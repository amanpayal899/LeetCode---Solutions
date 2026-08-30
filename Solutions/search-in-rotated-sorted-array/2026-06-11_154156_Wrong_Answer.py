# Problem: Search in Rotated Sorted Array
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-11_154156 UTC
# URL: https://leetcode.com/submissions/detail/2029902764/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif target < nums[mid] or target >= nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        return -1