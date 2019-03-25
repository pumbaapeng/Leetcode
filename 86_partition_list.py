class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fh_lt = ListNode(-1)
        fh_ge = ListNode(-1)
        ins_lt = fh_lt
        ins_ge = fh_ge
        cur = head
        while cur:
            if cur.val < x:
                ins_lt.next = cur
                ins_lt = cur
            else:
                ins_ge.next = cur
                ins_ge = cur
            cur = cur.next
        ins_ge.next = None
        ins_lt.next = fh_ge.next
        return fh_lt.next

