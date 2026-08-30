# Problem: Maximum Product of Two Elements in an Array
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-27_190436 UTC
# URL: https://leetcode.com/submissions/detail/2083866905/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstLarge = float('-inf')
        secondLarge = float('-inf')
        n = len(nums)
        for i in range(n):
            if nums[i]-1 >= firstLarge:
                secondLarge = firstLarge
                firstLarge = nums[i]-1
        return firstLarge*secondLarge
    
