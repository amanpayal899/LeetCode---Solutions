# Problem: Search in Rotated Sorted Array II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-12_120325 UTC
# URL: https://leetcode.com/submissions/detail/2030780727/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[mid] > nums[low]:
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