# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      # Optimial solution using Divide and Conquer
      # Merge the first and second of the lists, and repeat
      if lists is None or len(lists) == 0:
        return None
      while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
          # Does a partner exist at index i + 1?
          if i + 1 < len(lists):
            # Yes: merge the pair
            mergedLists.append(self.mergeList(lists[i], lists[i + 1]))
          else:
            # No: odd list out, carry it directly to the next round!
            mergedLists.append(lists[i])

        lists = mergedLists
      return lists[0]

    def mergeList(self, l1, l2):
      dummy = ListNode()
      tail = dummy

      while l1 and l2:
          if l1.val < l2.val:
              tail.next = l1
              l1 = l1.next
          else:
              tail.next = l2
              l2 = l2.next
          tail = tail.next

      if l1:
          tail.next = l1
      if l2:
          tail.next = l2

      return dummy.next