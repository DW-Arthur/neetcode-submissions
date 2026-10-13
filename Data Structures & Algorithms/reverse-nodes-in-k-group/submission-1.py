# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

  def reverseKGroup(
      self, head: Optional[ListNode], k: int
  ) -> Optional[ListNode]:
    # Check if the very first group has k nodes
    kth = self.getKth(head, k)
    if not kth:
      return head  # Fewer than k nodes total

    # The 1st group's kth node is permanently our final return head!
    new_head = kth

    prev_group_tail = None
    curr = head

    while curr:
      # Check if a full group of k exists starting at curr
      kth = self.getKth(curr, k)
      if not kth:
        # Fewer than k nodes remaining: leave them as is and attach to previous group
        if prev_group_tail:
          prev_group_tail.next = curr
        break

      group_next = kth.next

      # Standard reversal of k nodes
      prev = group_next
      node = curr
      while node != group_next:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt

      # Stitch the previous group's tail to this group's new head (kth)
      if prev_group_tail:
        prev_group_tail.next = kth

      # The original head (curr) is now the tail of this reversed group
      prev_group_tail = curr
      curr = group_next

    return new_head

  def getKth(self, curr, k):
    while curr and k > 1:
      curr = curr.next
      k -= 1
    return curr
        