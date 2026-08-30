# Problem: First Missing Positive
# Status: Accepted
# Language: python3
# Runtime: 43 ms
# Memory: 30.9 MB
# Submitted: 2026-03-19_184219 UTC
# URL: https://leetcode.com/submissions/detail/1953345475/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(0,len(nums)):
            if ( nums[i]<=0 or nums[i]==nums[i-1] and i!=0 ):
                continue
            elif ( nums[i]!= count):
                return count
            count += 1
        return count


