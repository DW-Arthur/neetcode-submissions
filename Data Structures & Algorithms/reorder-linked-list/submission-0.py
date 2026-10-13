# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Using an array, I store all the nodes,
        # Then use left and right pointers to swap.
        # In an normal array, I would just need to do temp = array[l] array[l] = array[r]...
        # In this LinkedList, I have to figure out how to swap with a pointer
        curr = head
        store = []
        while curr:
            store.append(curr)
            curr = curr.next
        l,r = 0, len(store) -1
        # left points to right
        # Then check if l is still < r, other wise they might be pointing at the same index
        # Then move left pointer forward
        # have left pointer point to array[l]
        # move both left pointer and right pointer
        while l <r:
            store[l].next = store[r]
            l +=1
            if l>=r:
                break 
            store[r].next = store[l]
            r-=1
        # Sever the last node to prevent an infinite cycl
        store[l].next = None



        