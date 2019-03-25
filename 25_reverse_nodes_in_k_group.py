# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fh = ListNode(-1)
        fh.next = head
        before, after = fh, fh.next
        while True:
            for i in range(k):
                if after:
                    after = after.next
                else:
                    return fh.next
            cur, next = before.next, before.next.next
            for i in range(k-1):
                next_cur, next_next = next, next.next
                next.next = cur
                cur, next = next_cur, next_next
            before.next.next = after
            before.next, before = cur, before.next


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
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)
    out = Solution().reverseKGroup(list1, 2)
    print_list(out)
