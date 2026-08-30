# Problem: Palindrome Linked List
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-01_193813 UTC
# URL: https://leetcode.com/submissions/detail/2052782478/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward_no = 0
        curr = head
        while curr is not None:
            forward_no = forward_no*10 + int(curr.val)
            curr = curr.next
        reverse = 0
        temp1 = copy.copy(forward_no)
        while temp1 != 0:
            reverse = reverse * 10 + temp1 % 10
            temp1 //= 10

        if forward_no == reverse:
            return True
        while forward_no % 10 == 0:
            forward_no //= 10

        while reverse % 10 == 0:
            reverse //= 10
        
        return forward_no == reverse

