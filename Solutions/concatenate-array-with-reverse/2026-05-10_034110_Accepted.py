# Problem: Concatenate Array With Reverse
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Submitted: 2026-05-10_034110 UTC
# URL: https://leetcode.com/submissions/detail/1999404097/

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = nums + [0]*length
        for i in range(length):
            ans[length+i] = nums[length - i-1]
        return ans
        