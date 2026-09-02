# Problem: Construct Uniform Parity Array I
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Submitted: 2026-09-02_193400 UTC
# URL: https://leetcode.com/submissions/detail/2128911089/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len(nums1) == 1:
            return True
        odd = -1
        even = -1
        for i in nums1:
            if i%2 == 0:
                even = 1
            else:
                odd = 1
        if (even and odd == 0) or (odd and even==0) or (even  and odd):
            return True


        