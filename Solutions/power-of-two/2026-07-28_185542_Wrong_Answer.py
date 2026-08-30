# Problem: Power of Two
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-28_185542 UTC
# URL: https://leetcode.com/submissions/detail/2085263008/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = n &(n-1)
        if result == 0:
            return True
        return False