# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force
        # Go through list1 and list 2, add the values together
        # Add the two values together, and update list 1 values
        # If the sum of the 2 nodes' values are more than 10, add a carry for the next node
        # If there is no Node on the next, make a new Node with 1 as the carry
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Continue as long as there is any digit or carry left to process
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
