# Problem: Linked List Cycle II
# Status: Accepted
# Language: python3
# Runtime: 56 ms
# Memory: 22.2 MB
# Submitted: 2026-06-20_191706 UTC
# URL: https://leetcode.com/submissions/detail/2040222733/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None