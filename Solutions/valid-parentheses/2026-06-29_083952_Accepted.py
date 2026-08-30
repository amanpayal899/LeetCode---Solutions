# Problem: Valid Parentheses
# Status: Accepted
# Language: python3
# Runtime: 1 ms
# Memory: 19.3 MB
# Submitted: 2026-06-29_083952 UTC
# URL: https://leetcode.com/submissions/detail/2049814333/

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = deque()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                my_stack.append(i)
            else:
                if not my_stack:
                    return False
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