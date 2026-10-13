# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # For this problem, no need to create a dummynode
        # Just make a the pointeres in the original list turn around
        prev = None
        curr = head
        while curr:
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
        return prev
        

