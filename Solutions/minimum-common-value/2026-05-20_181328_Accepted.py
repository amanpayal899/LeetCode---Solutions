# Problem: Minimum Common Value
# Status: Accepted
# Language: python3
# Runtime: 763 ms
# Memory: 37.8 MB
# Submitted: 2026-05-20_181328 UTC
# URL: https://leetcode.com/submissions/detail/2008422322/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums1:
            for j in nums2:
                if j>i:
                    break
                elif i==j:
                    return i 
        return -1