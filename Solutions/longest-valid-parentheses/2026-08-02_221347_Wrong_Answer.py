# Problem: Longest Valid Parentheses
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-02_221347 UTC
# URL: https://leetcode.com/submissions/detail/2091906818/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        my_stack = []
        longest = 0
        temp_longest = 0
        result = 0
        for i in range(l):
            if s[i] == '(':
                my_stack.append(s[i])
            else:
                if not my_stack:
                    result = max(longest, result)
                    longest = 0
                    continue
                if my_stack:
                    my_stack.pop()
                    temp_longest += 2
                if not my_stack:
                    longest += temp_longest
                    temp_longest = 0
        result = max(result, temp_longest, longest)
        return result
                
            
            