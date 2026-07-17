class MyStack:

    def __init__(self):
        self.myList = []

    def push(self, x: int) -> None:
        self.myList.append(x)

    def pop(self) -> int:
        return self.myList.pop()

    def top(self) -> int:
        return self.myList[-1]

    def empty(self) -> bool:
        if len(self.myList)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
