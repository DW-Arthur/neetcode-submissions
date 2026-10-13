# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        # Have the first pointer advance n steps
        first, second = head, head
        for i in range(n):
            if first:
                first = first.next
        # Once first reaches n step
        prev = curr
        while first:
            prev = second
            first = first.next
            second = second.next
        print(second.val)
        prev.next = second.next
        second.next = None
        return dummy.next