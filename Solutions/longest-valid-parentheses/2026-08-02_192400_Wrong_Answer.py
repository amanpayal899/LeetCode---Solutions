# Problem: Longest Valid Parentheses
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-02_192400 UTC
# URL: https://leetcode.com/submissions/detail/2091824865/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        my_stack = []
        longest = 0
        temp_longest = 0
        for i in range(l):
            if s[i] == '(':
                my_stack.append(s[i])
            else:
                if len(my_stack) != 0:
                    my_stack.pop()
                    temp_longest += 2
                    longest = max(longest, temp_longest)
                else:
                    temp_longest = 0

        return longest
                
            
            