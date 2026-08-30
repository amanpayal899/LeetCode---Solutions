# Problem: Process String with Special Operations I
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 23.2 MB
# Submitted: 2026-06-16_190624 UTC
# URL: https://leetcode.com/submissions/detail/2035584045/

class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for i in s:
            if (ord("a") <= ord(i) <= ord("z")) or (ord("A") <= ord(i) <= ord("Z")):
                result += i
            elif i == "*":
                result = result[:-1]
            elif i == "#":
                result = 2 * result
            elif i == "%":
                result = result[::-1]
        return result
