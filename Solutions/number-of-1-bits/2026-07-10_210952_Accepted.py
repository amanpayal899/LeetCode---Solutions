# Problem: Number of 1 Bits
# Status: Accepted
# Language: python3
# Runtime: 4 ms
# Memory: 19.2 MB
# Submitted: 2026-07-10_210952 UTC
# URL: https://leetcode.com/submissions/detail/2063309910/

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        temp = copy.copy(n)
        while temp>0:
            c += 1
            temp = (((~temp)+1)^temp)&temp
        return c