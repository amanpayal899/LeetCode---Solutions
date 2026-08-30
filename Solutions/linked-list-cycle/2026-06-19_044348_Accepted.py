# Problem: Linked List Cycle
# Status: Accepted
# Language: python3
# Runtime: 58 ms
# Memory: 22.9 MB
# Submitted: 2026-06-19_044348 UTC
# URL: https://leetcode.com/submissions/detail/2038235978/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_map = set()
        fast = head
        while fast is not None:
            if fast in hash_map:
                return True
            hash_map.add(fast)
            fast = fast.next
        return False