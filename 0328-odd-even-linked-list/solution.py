# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head
        even = odd.next
        even_head = even
        while odd.next is not None and even.next is not None:
            odd.next = odd.next.next
            temp = odd
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        if odd is None:
            temp.next = even_head
            even.next = None
        else:
            odd.next = even_head
        return head
