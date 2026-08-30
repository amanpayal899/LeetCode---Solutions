# Problem: Longest Valid Parentheses
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-02_205126 UTC
# URL: https://leetcode.com/submissions/detail/2091876196/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        stack = []
        count = 0
        longest = 0
        for i in range(l):
            if s[i]=='(':
                stack.append(i)
            elif stack and s[i] == ')':
                stack.pop()
                count += 1
            if not stack:
                longest += count
                count = 0
            else:
                longest = max(longest, count)

        return 2*longest
                    
            

