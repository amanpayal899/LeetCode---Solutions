# Problem: Sum of Compatible Numbers in Range I
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-07_031409 UTC
# URL: https://leetcode.com/submissions/detail/2024909579/

class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum = 0
        x = 1
        while abs(n - x) <= k:
            if x & n == 0:
                sum += x
            x += 1
        return sum