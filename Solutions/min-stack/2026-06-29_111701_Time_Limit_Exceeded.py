# Problem: Min Stack
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-29_111701 UTC
# URL: https://leetcode.com/submissions/detail/2049979487/

class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        if value < self.min:
            self.min = value
        self.my_stack.append(value)

    def pop(self) -> None:
        return self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        if self.min in self.my_stack:
            return self.min
        
        self.min = float('inf')
        for i in self.my_stack:
            if i < self.min:
                self.min = i
        return self.min

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()