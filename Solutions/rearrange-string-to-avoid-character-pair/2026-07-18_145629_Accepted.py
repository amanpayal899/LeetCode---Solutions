# Problem: Rearrange String to Avoid Character Pair
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.3 MB
# Submitted: 2026-07-18_145629 UTC
# URL: https://leetcode.com/submissions/detail/2072388461/

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        t = ""
        xString = ""
        n = len(s)
        for i in range(n):
            if s[i] == x:
                xString += x
            else:
                t += s[i]
        t = t+xString
        return t