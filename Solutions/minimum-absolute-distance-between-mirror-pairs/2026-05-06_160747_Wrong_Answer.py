# Problem: Minimum Absolute Distance Between Mirror Pairs
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-06_160747 UTC
# URL: https://leetcode.com/submissions/detail/1996719597/

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        length = len(nums)
        min = -1
        for i in range(0,length):
            
            for j in range(i+1,length):
                rev = 0
                current = nums[j]
                while current != 0:
                    rev = rev*10 +  current%10
                    current /= 10
                if (rev == nums[i] and min > j-i) or min == -1 :
                    min = j - i
        return min

                