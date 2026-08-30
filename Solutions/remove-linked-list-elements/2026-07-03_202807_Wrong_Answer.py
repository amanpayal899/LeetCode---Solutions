# Problem: Remove Linked List Elements
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-03_202807 UTC
# URL: https://leetcode.com/submissions/detail/2055090559/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.val == val:
            return None
        curr = head
        prev = None
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            prev = curr
            curr = curr.next
        return head