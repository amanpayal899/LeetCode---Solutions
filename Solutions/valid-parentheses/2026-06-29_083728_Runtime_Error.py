# Problem: Valid Parentheses
# Status: Runtime Error
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-29_083728 UTC
# URL: https://leetcode.com/submissions/detail/2049811932/

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = deque()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                my_stack.append(i)
            else:
                curr = my_stack.pop()
                if curr == '(' and i == ')':
                    continue
                if curr == '[' and i == ']':
                    continue
                if curr == '{' and i == '}':
                    continue
                else:
                    return False
        if not my_stack:
            return True
        return False