# Problem: Maximum Subarray
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-04_112410 UTC
# URL: https://leetcode.com/submissions/detail/2022227274/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for i in nums:
            if sum + i > 0:
                sum += i
                if sum > max_sum:
                    max_sum = sum
            else:
                sum = 0

        return max_sum
                