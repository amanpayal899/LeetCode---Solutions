# Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
# Status: Runtime Error
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-11_202220 UTC
# URL: https://leetcode.com/submissions/detail/2103415583/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        while i<l and ( nums[i]==nums[i+1]-1):
            i+=1
        prefixSum = sum(nums[:i+1])
        numsSet = set(nums)
        while prefixSum in numsSet:
            prefixSum += 1
        return prefixSum 