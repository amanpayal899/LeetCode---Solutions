# Problem: Linked List Cycle II
# Status: Accepted
# Language: python3
# Runtime: 59 ms
# Memory: 22.7 MB
# Submitted: 2026-06-19_080822 UTC
# URL: https://leetcode.com/submissions/detail/2038471627/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()
        current_node = head
        while current_node is not None:
            if current_node in my_set:
                return current_node
            my_set.add(current_node)
            current_node = current_node.next
        return None

        