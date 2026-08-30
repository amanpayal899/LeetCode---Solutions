# Problem: Maximum Subarray
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-03_182339 UTC
# URL: https://leetcode.com/submissions/detail/2021571397/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(n):
            total_sum = nums[i]
            if total_sum > max_sum:
                max_sum = total_sum
            for j in range(i+1,n):
                total_sum += nums[j]
                if total_sum > max_sum:
                    max_sum = total_sum
        return max_sum