class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        l, r = head, head
        prev = dummy

        # Fix 1: Move pointers to 1-indexed positions using `> 1` and `or`
        while left > 1 or right > 1:
            if left > 1:
                prev = l
                l = l.next
                left -= 1
            if right > 1:
                r = r.next
                right -= 1

        # r is now at position `right`, l is at position `left`
        nxt = r.next

        # Fix 2: `l` (the original start) will become the tail after reversal
        saveTail = l  

        # Fix 3: Reverse up to and INCLUDING `r` (stop when l moves past r)
        previous = None
        while previous != r:
            tmp = l.next
            l.next = previous
            previous = l
            l = tmp

        # Fix 4: Reconnect properly:
        # - `previous` ends up as `r` (the new head of the sublist)
        # - `saveTail` ends up pointing to `nxt`
        prev.next = previous
        saveTail.next = nxt

        return dummy.next