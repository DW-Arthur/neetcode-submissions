# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def reverseBetween(
      self, head: Optional[ListNode], left: int, right: int
  ) -> Optional[ListNode]:
    if not head or left == right:
      return head

    # 1. Dummy node handles left == 1 seamlessly
    dummy = ListNode(0, head)
    prev = dummy
    l = head
    r = head
    nxt = None

    curr = head
    k = 1

    # 2. Capture boundary pointers during traversal
    while curr:
      if k == left - 1:
        prev = curr
      if k == left:
        l = curr
      if k == right:
        r = curr
        nxt = curr.next
        break  # We have all the boundaries we need, no need to traverse further
      curr = curr.next
      k += 1

    # 3. Dedicated reverse helper
    def reverse(start, end_next):
      p = end_next  # Setting this to nxt automatically connects l.next -> nxt!
      c = start
      while c != end_next:
        tmp = c.next
        c.next = p
        p = c
        c = tmp
      return p  # Returns the new head (which will be 'r')

    # 4. Reverse the segment and stitch
    new_head = reverse(l, nxt)
    prev.next = new_head

    return dummy.next