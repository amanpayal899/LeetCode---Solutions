# Problem: Two Sum
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 20.5 MB
# Submitted: 2026-06-03_164120 UTC
# URL: https://leetcode.com/submissions/detail/2021457170/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        n = len(nums)
        for i in range(0, n):
            conjugate = target - nums[i]
            if conjugate in hash_table:
                return [i, hash_table[conjugate]]
            hash_table[nums[i]] = i
        