# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        current = head
        while current is not None and current.next is not None:
            slow = slow.next
            current = current.next.next
        return slow
        
        
