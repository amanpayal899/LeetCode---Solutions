# Problem: Search in Rotated Sorted Array II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-12_040317 UTC
# URL: https://leetcode.com/submissions/detail/2030325394/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n= len(nums)
        low, high = 0, n - 1

        
        while  low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True
            if mid == 0:
                low = mid + 1
            elif mid == n - 1:
                high = mid - 1
            elif nums[mid] > nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False