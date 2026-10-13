# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

  def reverseKGroup(
      self, head: Optional[ListNode], k: int
  ) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    groupPrev = dummy

    while True:
      # Step 1: Count ahead to verify at least k nodes remain
      kth = self.getKth(groupPrev, k)
      if not kth:
        break  # Fewer than k nodes left -> leave them untouched!

      groupNext = kth.next

      # Step 2: Reverse the k-group (standard iterative reversal)
      prev = groupNext  # Pointing directly to groupNext auto-connects the tail!
      curr = groupPrev.next
      while curr != groupNext:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

      # Step 3: Reconnect the previous group to the new head of this group
      tmp = groupPrev.next  # This was the old head, now it is the new tail
      groupPrev.next = (
          kth  # kth is the new head of this group after reversing
      )
      groupPrev = tmp  # Move groupPrev to the tail for the next round

    return dummy.next

  def getKth(self, curr, k):
    while curr and k > 0:
      curr = curr.next
      k -= 1
    return curr