# Problem: Remove Nth Node From End of List
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-06-21_185836 UTC
# URL: https://leetcode.com/submissions/detail/2041340669/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        curr_node = head
        count = 0
        my_list = []
        while curr_node is not None:
            my_list.append(curr_node)
            curr_node = curr_node.next
            count += 1
        if count - n == 0:
            return head.next
        changed_node = my_list[count - n - 1]
        changed_node.next = changed_node.next.next
        return head
        