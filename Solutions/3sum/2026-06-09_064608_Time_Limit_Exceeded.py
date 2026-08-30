# Problem: 3Sum
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-09_064608 UTC
# URL: https://leetcode.com/submissions/detail/2027171152/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        final = []
        n = len(nums)
        i, j, k = 0, 1, 2
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] +nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        temp = tuple(temp)
                        result.add(temp)
        final = [ list(i) for i in result ]  
        return final