class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        fh = ListNode(-1)
        fh.next = head
        prev = fh
        while prev and prev.next:
            cur = prev.next
            deleted = False
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
                deleted = True
            if not deleted:
                prev = prev.next
            else:
                prev.next = cur.next
        return fh.next
