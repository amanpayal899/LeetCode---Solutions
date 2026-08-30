# Problem: Minimum Common Value
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-20_181040 UTC
# URL: https://leetcode.com/submissions/detail/2008419759/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums1:
            for j in nums2:
                if j>i:
                    break
                elif i==j:
                    return i    