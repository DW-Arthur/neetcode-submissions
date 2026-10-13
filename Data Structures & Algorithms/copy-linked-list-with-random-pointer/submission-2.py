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
        # Use a dictionary to copy the linkedlist with random pointer
        # Use a dummy Node at the begining
        # First pass is to add all the pointers in the dictionary
        # The space is the dictionary size of the original linkedlist
        # The first pass, just pass the values in, don't worry about next or random
        # Second pass, connect the random and .next using the dictionary
        # The dictionary should be initiated with None: None, so if a node is asking
        # it's .next or random is None, it would return none
        # The None:None is used so that we don;t have to add a if/else statement
        # everytime we reached None
        store = {None: None}
        dummy = Node(0)
        curr = head
        first = dummy
        while curr:
            # Key will be curr, value will also be the curr?
            # Im storing the reference to the key, and the pointer as value
            # Perhaps I need to save the value as the value
            # Do i want the key, and the entire node as vakue
            store[curr] = Node(curr.val)
            # Do I create a dummy node
            curr = curr.next
        curr = head
        while curr:
            store[curr].next = store[curr.next]
            store[curr].random = store[curr.random]
            curr = curr.next
        return store[head]
            
        