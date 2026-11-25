# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Use 2 pointers, go through until one reaches the end, then append the end
        # If one pointer is smaller, connect the smaller to second, then move the smaller one forward, the smaller pointer stays?
        # Do I need an empty linkedlist?
        first, second = list1, list2
        # I need a dummy node
        dummy = ListNode(0)
        curr = dummy
        while first and second:
            if first.val <= second.val:
                curr.next = first
                curr = curr.next
                first = first.next
            else:
                curr.next = second
                curr = curr.next
                second = second.next
        if second:
            curr.next = second
        if first:
            curr.next =first
        return dummy.next