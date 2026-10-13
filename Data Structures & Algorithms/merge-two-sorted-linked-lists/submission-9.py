# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion Trust Fall method
        # I would assume to recursive call the function by passing list1 and list2 pointers
        # based on their values
        # I would assume the recursive function correctly recalls the newHead of the new list
        # When the newHead arrives, i would compare the list1 vs list2 values of the current 
        # stack, if one is too bigger, i would set the newHead to point to the sammller one
        # And add the bigger one after it
        # Base case would be if either list 1 or list 2 reaches None:
        # If it reaches None, return None? This informs the returning newHead that 
        # the end of the list is reached
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <=list2.val:
            result = self.mergeTwoLists(list1.next,list2)
            list1.next = result
            return list1
        else:
            result = self.mergeTwoLists(list1, list2.next)
            list2.next = result
            return list2
        
        


        