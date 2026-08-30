# Problem: Set Mismatch
# Status: Accepted
# Language: python3
# Runtime: 10 ms
# Memory: 20.6 MB
# Submitted: 2026-05-09_192201 UTC
# URL: https://leetcode.com/submissions/detail/1999182181/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = -1
        missing = -1
        my_list = [0]*(n+1)
        for num in nums:
            my_list[num] += 1
        for i in range(1,n+1):
            if my_list[i] == 2:
                duplicate = i
            if my_list[i] == 0:
                missing = i
        return [duplicate, missing]
