# Problem: Middle of the Linked List
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Submitted: 2026-06-18_161301 UTC
# URL: https://leetcode.com/submissions/detail/2037776248/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current_node = head
        while current_node != None:
            count += 1
            current_node = current_node.next
        mid = (count//2) + 1
        count = 0
        current_node = head
        while current_node != None:
            count += 1
            if count == mid:
                return current_node
            current_node = current_node.next
        return 

