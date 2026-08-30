# Problem: Middle of the Linked List
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-06-18_165452 UTC
# URL: https://leetcode.com/submissions/detail/2037825117/

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
        
        