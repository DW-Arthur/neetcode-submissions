# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # How to think recursion
        # Trust Fall
        # If im at first node, trust the recursion will give back the correct list
        # EX
        # My node: 1 ->2
        # Returned node: 3->2->None (new head is 3,return this new head, not 1)
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next =head
        head.next = None
        return new_head


