# Problem: Linked List Cycle
# Status: Accepted
# Language: python3
# Runtime: 50 ms
# Memory: 22.5 MB
# Submitted: 2026-06-19_055055 UTC
# URL: https://leetcode.com/submissions/detail/2038315305/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False