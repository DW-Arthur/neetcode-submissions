# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Keep a pointer to previous and nxt
        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                tmp = curr.next
                prev.next = tmp
                curr.next =None
                curr = tmp
                #prev = prev.next
                continue
            prev = curr
            curr = curr.next
        return dummy.next