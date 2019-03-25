# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        fh = ListNode(-1)
        fh.next = head
        list_len = 0
        while head:
            list_len += 1
            head = head.next
        if list_len == 0:
            return None
        k = k % list_len
        if k == 0:
            return fh.next
        mid = tail = fh
        for i in range(k):
            tail = tail.next
        while tail.next:
            tail = tail.next
            mid = mid.next
        fh.next, mid.next, tail.next = mid.next, None, fh.next
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
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)
    out = Solution().rotateRight(list1, 8)
    print_list(out)


