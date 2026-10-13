# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # From my drawing, when doing slow, fast poitners
        # If both start on head. On even list, the fast pointer will reach None
        # On odd list, the fast poitner will reach the last node, right before None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow