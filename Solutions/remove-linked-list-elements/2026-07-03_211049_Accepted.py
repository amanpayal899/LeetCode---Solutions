# Problem: Remove Linked List Elements
# Status: Accepted
# Language: python3
# Runtime: 7 ms
# Memory: 22.4 MB
# Submitted: 2026-07-03_211049 UTC
# URL: https://leetcode.com/submissions/detail/2055108760/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next
        curr = head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head