# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node is needed for iteration
        # Inititae Dummy Node first, have a poitner point to it
        # Have 2 pointers, list1 and list 2, iterate until one of the reaches None
        # Add the rest of the LinkedList to it 
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if not list1 and list2:
            curr.next = list2
        else:
            curr.next = list1
        return dummy.next

        