# Problem: Remove Nth Node From End of List
# Status: Runtime Error
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-06-21_185147 UTC
# URL: https://leetcode.com/submissions/detail/2041335483/

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
        changed_node = my_list[count - n - 1]
        changed_node.next = changed_node.next.next
        return head
        