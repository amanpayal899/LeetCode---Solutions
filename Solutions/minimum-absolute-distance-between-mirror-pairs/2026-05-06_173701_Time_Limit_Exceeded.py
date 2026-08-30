# Problem: Minimum Absolute Distance Between Mirror Pairs
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-06_173701 UTC
# URL: https://leetcode.com/submissions/detail/1996791687/

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        length = len(nums)
        min = -1
        for i in range(0,length):
            rev = 0
            current = nums[i]
            while current != 0:
                rev = rev*10 +  current%10
                current //= 10
            for j in range(i+1,length):
                
                if rev == nums[j] and ( min > j-i or min == -1):
                    min = j - i
        return min

                