# Problem: Min Stack
# Status: Accepted
# Language: python3
# Runtime: 148 ms
# Memory: 33 MB
# Submitted: 2026-06-29_182138 UTC
# URL: https://leetcode.com/submissions/detail/2050420757/

class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min = '#'

    def push(self, value: int) -> None:
        if self.min == '#':
            self.min = value
        elif self.min > value:
            self.min = value
        self.my_stack.append([value, self.min])

    def pop(self) -> None:
        self.my_stack.pop()
        if not self.my_stack:
            self.min = '#'
        else:
            self.min = self.my_stack[-1][1]


    def top(self) -> int:
       return self.my_stack[-1][0]
        

    def getMin(self) -> int:
        return self.my_stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()