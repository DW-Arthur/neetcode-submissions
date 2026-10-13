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
        # 2 passes, first put the old node as key and new node as value
        copy = {None:None}
        start = head
        while start:
            copy[start] = Node(start.val)
            start = start.next
        start = head
        while start:
            copy[start].next = copy[start.next]
            copy[start].random = copy[start.random]
            start = start.next
        return copy[head]
        

        