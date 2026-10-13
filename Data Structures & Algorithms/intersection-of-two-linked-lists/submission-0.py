# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Find the difference between the length of the list
        # Then move forward the longer one by the difference
        # This way if they will either intersect at Null or the same node
        def helper(curr):
            result = 0
            while curr:
                curr = curr.next
                result +=1
            return result
        lengthA = helper(headA)
        lengthB = helper(headB)
        if lengthA > lengthB:
            diff = lengthA- lengthB
            for i in range(0, diff):
                headA = headA.next
        elif lengthB > lengthA:
            diff = lengthB - lengthA
            for i in range(0, diff):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None