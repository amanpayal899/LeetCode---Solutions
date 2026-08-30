# Problem: Minimum Common Value
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-20_180746 UTC
# URL: https://leetcode.com/submissions/detail/2008417151/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums1:
            for j in nums2:
                if i==j:
                    return i    