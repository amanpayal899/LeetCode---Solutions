# Problem: Remove Linked List Elements
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-03_210707 UTC
# URL: https://leetcode.com/submissions/detail/2055107296/

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
                prev = curr.next
            else:
                prev = curr
            curr = curr.next
        return head