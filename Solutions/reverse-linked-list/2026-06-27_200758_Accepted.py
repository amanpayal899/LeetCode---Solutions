# Problem: Reverse Linked List
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 20.5 MB
# Submitted: 2026-06-27_200758 UTC
# URL: https://leetcode.com/submissions/detail/2048236032/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head.next
        prev = head
        prev.next = None
        while curr.next is not None:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
            
        curr.next = prev
        return curr