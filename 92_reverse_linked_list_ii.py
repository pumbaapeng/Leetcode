# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n <= m:
            return head
        fh = ListNode(-1)
        fh.next = head
        left = fh
        for i in range(m - 1):
            left = left.next
        right = left
        for i in range(n - m + 2):
            right = right.next
        cur, nxt = left.next, left.next.next
        for i in range(n - m):
            next_cur, next_nxt = cur.next, nxt.next
            nxt.next = cur
            cur, nxt = next_cur, next_nxt
        left.next.next = right
        left.next = cur
        return fh.next


