class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        first, second = self.split_into_two(head)
        second = self.reverse(second)
        return self.interleave(first,second)

    def split_into_two(self, head):
        fh = ListNode(-1)
        fh.next = head
        slow = fast = fh
        while fast and fast.next: # until fast is Null or the last valid node
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        head2 = slow.next
        slow.next = None
        return head, head2

    def reverse(self, head):
        if not head: return None
        fh = ListNode(-1)
        fh.next = head
        cur, nxt = head, head.next
        while cur and nxt:
            next_cur, next_nxt = nxt, nxt.next
            cur.next.next = cur
            cur, nxt = next_cur, next_nxt
        fh.next.next = None
        fh.next = cur
        return fh.next

    def interleave(self, head1, head2):
        fh1 = ListNode(-1)
        fh1.next = head1
        fh2 = ListNode(-1)
        fh2.next = head2
        while head1 is not None and head2 is not None:
            next_head1 = head1.next
            next_head2 = head2.next
            head1.next = head2
            head2.next = next_head1
            head1, head2 = next_head1, next_head2
        return fh1.next


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
    out = Solution().reorderList(list1)
    print_list(out)
