# Problem: Search in Rotated Sorted Array II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-12_034007 UTC
# URL: https://leetcode.com/submissions/detail/2030309463/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while  low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True
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