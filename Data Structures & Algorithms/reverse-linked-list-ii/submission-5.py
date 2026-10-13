# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
      if not head or left == right:
        return head
      dummy = ListNode(0, head)
      prev = dummy
      curr = head
      count = 1
      # I would need to get the previous node of left, for the right, I would need the right
      # node and the next node of the right pointer
      # Walk up to and including 'right'
      while curr and count <= right:
        if count == left:
          first_previous = prev
          first = curr
        if count == right:
          second_next = curr.next
          second = curr

        prev = curr
        curr = curr.next
        count += 1
      # Reverse the nodes starting for first to second
      previous = None
      tail = first
      while first != second_next:
        nxt = first.next
        first.next = previous
        previous = first
        first = nxt
      # First_previous points now points to the new head, which should be previous (second)
      # I think previous can be second here
      first_previous.next = previous
      #first ppointer is now the new tail after going through the reverseing loop
      tail.next = second_next
      # The new tail is 
      return dummy.next
        


        