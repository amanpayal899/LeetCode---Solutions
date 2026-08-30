# Problem: Largest Integer With Given Digit Sum
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-26_042843 UTC
# URL: https://leetcode.com/submissions/detail/2081516245/

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        
        if s > (n*9):
            return -1
        if s==0:
            return 0
        result = 0
        sum = n*9
        for _ in range(n):
            result = result*10 + 9

        
        while result != 0:
            if sum == s:
                return result
            sum -= result%10
            result -= 1
            sum = sum + result %10
        return -1
            