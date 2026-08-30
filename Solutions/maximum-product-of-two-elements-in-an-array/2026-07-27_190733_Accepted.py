# Problem: Maximum Product of Two Elements in an Array
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Submitted: 2026-07-27_190733 UTC
# URL: https://leetcode.com/submissions/detail/2083869676/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstLarge = float('-inf')
        secondLarge = float('-inf')
        n = len(nums)
        for i in range(n):
            if nums[i]-1 >= firstLarge:
                secondLarge = firstLarge
                firstLarge = nums[i]-1
            elif nums[i]-1 > secondLarge:
                secondLarge = nums[i]-1
        return firstLarge*secondLarge
    
