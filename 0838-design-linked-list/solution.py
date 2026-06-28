class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while curr is not None:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        return -1


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            new = Node(val)
            new.next = self.head
            self.head = new
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev = self.head
        curr = self.head.next
        count = 1
        while curr is not None:
            if count == index:
                prev.next = new_node
                new_node.next = curr
                return
            prev = curr
            curr = curr.next
            count += 1

        if count == index:
            prev.next = new_node
            new_node.next = curr
        return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        count = 1
        curr = self.head.next
        prev = self.head
        while curr is not None:
            if count == index:
                prev.next = curr.next
                return
            count += 1
            prev = curr
            curr = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
