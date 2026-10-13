class Solution:

  def addTwoNumbers(
      self, l1: Optional[ListNode], l2: Optional[ListNode]
  ) -> Optional[ListNode]:

    def add(
        n1: Optional[ListNode], n2: Optional[ListNode], carry: int
    ) -> Optional[ListNode]:
      # Base case: no digits left anywhere and no carry remains
      if not n1 and not n2 and carry == 0:
        return None

      # Extract values (default to 0 if a list is exhausted)
      v1 = n1.val if n1 else 0
      v2 = n2.val if n2 else 0

      # Calculate current digit and outgoing carry
      total = v1 + v2 + carry
      new_carry = total // 10

      # Create our node
      curr = ListNode(total % 10)

      # Trust Fall: next frame returns the rest of the chain
      next1 = n1.next if n1 else None
      next2 = n2.next if n2 else None
      curr.next = add(next1, next2, new_carry)

      return curr

    return add(l1, l2, 0)