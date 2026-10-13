# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Make 2 pointers
        # First pointer is at head, second is n steps ahead
        slow = head
        fast = head
        dummy = ListNode(0, head)
        for i in range(0, n):
            fast = fast.next
        prev = dummy
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        slow.next =None
        return dummy.next
        
        