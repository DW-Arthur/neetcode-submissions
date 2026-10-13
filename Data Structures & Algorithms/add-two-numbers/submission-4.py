# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iteratively
        # Go through l1 and l2, keep a dummy node
        # In case l1 is significatly shorter than l2
        dummy = ListNode(0)
        curr = dummy
        carry =0
        while l1 or l2:
            if l1 is None:
                n1 = 0
            else:
                n1 = l1.val
            if l2 is None:
                n2 = 0
            else:
                n2 = l2.val
            if n1 + n2 + carry>=10:
                result = (n1+n2) + carry- 10
                curr.next = ListNode(result)
                carry = 1 
                curr = curr.next
            else:
                result = n1+n2 + carry
                curr.next = ListNode(result)
                carry = 0 
                curr = curr.next
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
        