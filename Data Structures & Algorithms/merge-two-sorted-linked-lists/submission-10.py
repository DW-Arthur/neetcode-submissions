# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion trust fall method
        # I trust the returned recursion stack would return the correct newHead with
        # sorted merged linked lists
        # At the current stack, I would compare list1 and lsit 2 values, if it is smaller
        # list 1.next would connect to the newHead
        # For base case scenario
        # if list 1 is empty, return list 2, this is to connect the reamining smaller ones
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            newHead = self.mergeTwoLists(list1.next, list2)
            list1.next = newHead
            return list1
        else:
            newHead = self.mergeTwoLists(list1, list2.next)
            list2.next = newHead
            return list2
