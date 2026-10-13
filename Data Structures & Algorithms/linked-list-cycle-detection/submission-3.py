# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Assume the each node has a unique value, I would put the value in an array
        # Traverse the linkedlist, if I encounter a value that is already in the array
        # return True, if I reach None, false
        # In order for this to work, 
        # I need to store the node references(the object themselves)
        # Hashset is needed
        duplicate = set()
        curr = head
        while curr:
            if curr in duplicate:
                return True
            duplicate.add(curr)
            curr =curr.next
        return False

