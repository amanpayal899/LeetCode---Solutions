# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        list3 = None
        prev = None
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                if list3 is None:
                    list3 = p1
                    prev = p1
                else:
                    prev.next = p1
                    prev = p1
                p1 = p1.next
            else:
                if list3 is None:
                    list3 = p2
                    prev = p2
                else:
                    prev.next = p2
                    prev = p2
                p2 = p2.next
            
        
        if p1 is None:
            prev.next = p2
        else:
            prev.next = p1
        return list3





