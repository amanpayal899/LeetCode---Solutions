# Problem: Minimum Distance Between Three Equal Elements I
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-11_235114 UTC
# URL: https://leetcode.com/submissions/detail/1975849715/

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        true_distance=len(nums)
        for n in range(len(nums)-1):
            count = 1
            temp_distance=0
            for m in range(n+1,len(nums)-1):
                if count<3 and nums[m]==nums[n]:
                    count += 1
                    temp_distance = m-n
                if count>3:
                    break
            if temp_distance<true_distance:
                true_distance = temp_distance
        return true_distance

