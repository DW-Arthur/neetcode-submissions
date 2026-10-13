class Solution:

  def reorderList(self, head: Optional[ListNode]) -> None:
    if not head or not head.next:
      return

    self.left = head
    self.stop = False  # Flag to stop rewiring once middle is reached

    def recurse(right: Optional[ListNode]):
      if not right:
        return

      # Trust fall: Go all the way to the end of the list
      recurse(right.next)

      # ─── UNWINDING PHASE (Post-Order) ───

      # If we already finished the middle, do nothing as stack unwinds
      if self.stop:
        return

      # Stop condition 1: Odd length middle (left and right meet at same node)
      if self.left == right:
        right.next = None
        self.stop = True
        return

      # Stop condition 2: Even length middle (left is immediately before right)
      if self.left.next == right:
        right.next = None
        self.stop = True
        return

      # Rewire: insert 'right' right after 'self.left'
      nxt = self.left.next
      self.left.next = right
      right.next = nxt

      # Move self.left forward for the next stack frame above us
      self.left = nxt

    recurse(head)