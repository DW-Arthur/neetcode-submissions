# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def rec(prev, root):
            if not root.next:
                root.next = prev
                return root
            future = root.next
            root.next = prev
            return rec(root, future)
        return rec(None, head)

        