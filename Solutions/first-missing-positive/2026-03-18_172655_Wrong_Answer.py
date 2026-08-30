# Problem: First Missing Positive
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-18_172655 UTC
# URL: https://leetcode.com/submissions/detail/1952338214/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(len(nums)):
            if ( nums[i]<=0 or nums[i]==nums[i-1] ):
                continue
            if ( nums[i]!= count):
                break
            count += 1
        return count


