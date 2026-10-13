class Solution:

  def reverseBetween(
      self, head: Optional[ListNode], left: int, right: int
  ) -> Optional[ListNode]:
    if not head or left == right:
      return head

    # 1. Helper defined first
    def reverse(start_node: ListNode, steps: int):
      # We need to reverse (steps + 1) nodes total
      p = None
      c = start_node
      for _ in range(steps + 1):
        nxt = c.next
        c.next = p
        p = c
        c = nxt

      # p is now the new head of the reversed segment
      # c is the first node of the remainder list
      # start_node is now the tail of the reversed segment!
      start_node.next = c
      return p

    # 2. Main 1-pass loop
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    k = 1

    while curr:
      if k == left:
        new_head = reverse(curr, right - left)
        prev.next = new_head
        break

      prev = curr
      curr = curr.next
      k += 1

    return dummy.next