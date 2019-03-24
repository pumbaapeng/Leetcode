class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        fh = ListNode(-1)
        fh.next = head
        prev, cur = fh, fh.next
        while cur and cur.next:
            next_cur, next_prev = cur.next.next, cur
            prev.next = cur.next
            cur.next.next = cur
            cur.next = next_cur
            cur, prev = next_cur, next_prev
        return fh.next


def print_list(head):
    cur = head
    out = []
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" ".join(out))


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list1.next.next.next = ListNode(5)
    out = Solution().swapPairs(list1)
    print_list(out)
