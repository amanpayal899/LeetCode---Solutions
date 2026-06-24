# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def integer(self, curr_node):
        if curr_node.next is None:
            return curr_node.val 
        return self.integer(curr_node.next)*10 + curr_node.val

    def l3(self, num):
        if num//10 == 0:
            node = ListNode(num%10, None)
            return node
        node = ListNode(num%10,self.l3(num//10))
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = self.integer(l1)
        n2 = self.integer(l2)
        summ = n1+n2
        return self.l3(summ)

