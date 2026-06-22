# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        while n > 0:
            second = second.next
            n -= 1
        if second is None:
            return head.next
        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head

        

