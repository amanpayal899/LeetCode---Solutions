# Problem: Maximum Subarray
# Status: Accepted
# Language: python3
# Runtime: 15 ms
# Memory: 31.3 MB
# Submitted: 2026-06-04_113044 UTC
# URL: https://leetcode.com/submissions/detail/2022232194/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for i in nums:
            if sum + i > i:
                sum += i
                
            else:
                sum = i
            if sum > max_sum:
                max_sum = sum

        return max_sum
                