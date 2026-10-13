# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute Force
        dummy = ListNode(0)
        dummy.next = head
        # 1. Collect dummy + all nodes
        seen = []
        curr = dummy
        while curr:
            seen.append(curr)
            curr = curr.next

        # 2. Total items in seen is len + 1.
        # The node directly before target is at index: len(seen) - n - 1
        prev = seen[len(seen) - n - 1]
        prev.next = prev.next.next

        return dummy.next

        