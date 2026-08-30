# Problem: Odd Even Linked List
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 21.2 MB
# Submitted: 2026-06-20_203936 UTC
# URL: https://leetcode.com/submissions/detail/2040268108/

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