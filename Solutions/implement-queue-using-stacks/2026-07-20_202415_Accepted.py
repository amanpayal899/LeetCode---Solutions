# Problem: Implement Queue using Stacks
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-07-20_202415 UTC
# URL: https://leetcode.com/submissions/detail/2075069562/

class MyQueue:

    def __init__(self):
        self.arr = deque([])

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        return self.arr.popleft()

    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()