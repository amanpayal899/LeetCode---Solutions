# Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.3 MB
# Submitted: 2026-08-11_202305 UTC
# URL: https://leetcode.com/submissions/detail/2103416013/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        while i<l-1 and ( nums[i]==nums[i+1]-1):
            i+=1
        prefixSum = sum(nums[:i+1])
        numsSet = set(nums)
        while prefixSum in numsSet:
            prefixSum += 1
        return prefixSum 