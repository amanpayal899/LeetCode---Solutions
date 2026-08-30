# Problem: Search in Rotated Sorted Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Submitted: 2026-06-11_161420 UTC
# URL: https://leetcode.com/submissions/detail/2029936379/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1