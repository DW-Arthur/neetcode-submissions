# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative 3 pointer method,
        # next, prev, curr node
        # next node holds next, prev holds prev, curr move around
        # setup, prev = None, curr = head
        prev, curr = None, head
        while curr:
            nxt= curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


