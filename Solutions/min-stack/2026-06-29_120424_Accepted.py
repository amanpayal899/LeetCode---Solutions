# Problem: Min Stack
# Status: Accepted
# Language: python3
# Runtime: 117 ms
# Memory: 31.9 MB
# Submitted: 2026-06-29_120424 UTC
# URL: https://leetcode.com/submissions/detail/2050022201/

class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_stack = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        if value <= self.min:
            self.min = value
            self.min_stack.append(value)
        self.my_stack.append(value)

    def pop(self) -> None:
        popped = self.my_stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
            if  self.min_stack:
                self.min = self.min_stack[-1]
            else:
                self.min = float('inf')
        return popped

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()