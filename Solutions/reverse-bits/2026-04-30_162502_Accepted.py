# Problem: Reverse Bits
# Status: Accepted
# Language: python3
# Runtime: 34 ms
# Memory: 19 MB
# Submitted: 2026-04-30_162502 UTC
# URL: https://leetcode.com/submissions/detail/1991950175/

class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(0,32):
            rev <<= 1
            rev = rev | (n&1)
            n >>= 1
           
        return rev