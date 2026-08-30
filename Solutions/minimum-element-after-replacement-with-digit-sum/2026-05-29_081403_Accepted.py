# Problem: Minimum Element After Replacement With Digit Sum
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Submitted: 2026-05-29_081403 UTC
# URL: https://leetcode.com/submissions/detail/2016225690/


def digit_sum(num):
    if num//10 == 0:
        return num
    return num%10 + digit_sum(num//10)
class Solution:
    def minElement(self, nums: List[int]) -> int:
        length = len(nums)
        min = nums[0]
        for i in range(0, length):
            nums[i] = digit_sum(nums[i])
            if(nums[i] < min):
                min = nums[i]
        return min