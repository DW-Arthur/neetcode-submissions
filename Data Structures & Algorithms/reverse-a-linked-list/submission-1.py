# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Make a while loop, go to the end of the list, once at the end, have a pointer
        # point to the index, then go backwards
        # Make a new value? Like a new list?
        # There's no previous, not doubly linked list. Maybe make a copy of the entire list
        # Then use the head to point it to the back?
        # Make an array? record all he values
        # once recored
        # Make a linkedlist, starting from the last to first
        if not head:
            return None

        # 1. Collect all node values
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # 2. Build a new linked list in reverse order
        new_head = ListNode(values[-1])
        curr = new_head
        for i in range(len(values) - 2, -1, -1):
            curr.next = ListNode(values[i])
            curr = curr.next

        return new_head

