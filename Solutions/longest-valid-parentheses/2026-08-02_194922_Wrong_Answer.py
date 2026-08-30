# Problem: Longest Valid Parentheses
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-02_194922 UTC
# URL: https://leetcode.com/submissions/detail/2091842537/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        my_stack = []
        longest = 0
        temp_longest = 0
        count = 0
        for i in range(l):
            if s[i] == '(':
                my_stack.append(s[i])
            else:
                if len(my_stack) != 0:
                    my_stack.pop()
                    temp_longest += 2
                    
                    
                if len(my_stack)==0:
                    longest += temp_longest 
                    temp_longest = 0
        if longest == 0:
            return temp_longest
        return longest
                
            
            