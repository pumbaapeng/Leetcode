# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        print("node with val", self.val, "destroyed")
        self.val = -1
        self.next = None


# Lessons learned:
# 1) use fake head
# 2) return fake_head.next
# 3) initialize cur, end properly (i.e., cur = fh, end = head)


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fh = ListNode(-1)
        fh.next = head
        cur = fh
        end = head
        for i in range(n):
            end = end.next
        while end:
            end = end.next
            cur = cur.next
        to_delete = cur.next
        cur.next = to_delete.next
        return fh.next


if __name__ == '__main__':
    head = ListNode(99)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    new_head = Solution().removeNthFromEnd(head, 1)
    cur = new_head
    while cur:
        print(cur.val)
        cur = cur.next
    print(head.val)
