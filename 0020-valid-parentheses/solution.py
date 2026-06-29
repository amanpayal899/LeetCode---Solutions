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
