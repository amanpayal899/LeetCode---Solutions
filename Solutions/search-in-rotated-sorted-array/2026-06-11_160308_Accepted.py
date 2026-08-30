# Problem: Search in Rotated Sorted Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Submitted: 2026-06-11_160308 UTC
# URL: https://leetcode.com/submissions/detail/2029924453/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high= mid - 1
                else:
                    low = mid + 1
        return -1