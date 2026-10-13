"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Use a dictionary to store all the nodes in the first pass
        # The use the first pass to point the .next pointer for all nodes
        # Then use the second pass to point the .random pointer.
        copy = {None: None}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        # Copy[curr], the original node is the key, it points to the new copied node
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next
        return copy[head]

        