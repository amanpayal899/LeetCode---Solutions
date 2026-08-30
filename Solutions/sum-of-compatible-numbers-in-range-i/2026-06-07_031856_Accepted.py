# Problem: Sum of Compatible Numbers in Range I
# Status: Accepted
# Language: python3
# Runtime: 7 ms
# Memory: 19.5 MB
# Submitted: 2026-06-07_031856 UTC
# URL: https://leetcode.com/submissions/detail/2024915341/

class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum = 0
        x = 1
        while x <= k+n:
            if (abs(n - x) <= k) and (x & n == 0):
                sum += x
            x += 1
        return sum