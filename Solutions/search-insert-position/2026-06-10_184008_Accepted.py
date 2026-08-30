# Problem: Search Insert Position
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.9 MB
# Submitted: 2026-06-10_184008 UTC
# URL: https://leetcode.com/submissions/detail/2028994545/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lb = n
        low = 0
        high = n-1
        while low <= high:
            mid = (high - low)//2 + low
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb