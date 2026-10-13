# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Since the two linked list are sorted , have 2 pointers, 1 pointer for each linked list
        # Compare the 2 pointers, if 1 is smaller than the other, add that pointer
        # to the result list, and move the smaller pointer forward
        # repeat until both point reached now
        
        # Create a new result linkedlist
        dummy = ListNode()  # dummy node to simplify logic
        current = dummy     # pointer to build the result list

        first = list1
        second = list2

        while first and second:
            if first.val <= second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next  # move current forward

        # One of the lists might still have nodes left
        if first:
            current.next = first
        if second:
            current.next = second

        return dummy.next  # skip dummy node and return actual head