# Problem: Power of Two
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Submitted: 2026-07-28_185652 UTC
# URL: https://leetcode.com/submissions/detail/2085264149/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        result = n &(n-1)
        if result == 0:
            return True
        return False