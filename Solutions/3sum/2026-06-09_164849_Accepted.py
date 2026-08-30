# Problem: 3Sum
# Status: Accepted
# Language: python3
# Runtime: 2966 ms
# Memory: 24 MB
# Submitted: 2026-06-09_164849 UTC
# URL: https://leetcode.com/submissions/detail/2027755984/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        list_set = set()
        n = len(nums)
        for i in range(0, n-1):
            num_set = set()
            for j in range(i+1, n):
                third = -(nums[i] + nums[j])
                if third in num_set:
                    temp_list = [nums[i], nums[j], third]
                    temp_list.sort()
                    list_set.add(tuple(temp_list))
                else:
                    num_set.add(nums[j])
        result = [list(i) for i in list_set]
        return result