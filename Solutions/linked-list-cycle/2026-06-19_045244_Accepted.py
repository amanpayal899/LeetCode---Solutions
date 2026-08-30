# Problem: Linked List Cycle
# Status: Accepted
# Language: python3
# Runtime: 49 ms
# Memory: 22.4 MB
# Submitted: 2026-06-19_045244 UTC
# URL: https://leetcode.com/submissions/detail/2038246808/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast is not None:
            if fast.val == '#':
                return True
            fast.val = '#'
            fast = fast.next
        return False