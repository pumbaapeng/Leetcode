# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.find_mid_point(head)
        head2 = mid.next
        mid.next = None
        return self.merge_sorted_lists(self.sortList(head), self.sortList(head2))

    def find_mid_point(self, head): #input has len >= 1
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        idx = (count - 1) // 2
        cur = head
        for i in range(idx):
            cur = cur.next
        return cur

    def merge_sorted_lists(self, head1, head2):
        fh = ListNode(-1)
        prev = fh
        while head1 and head2:
            if head1.val < head2.val:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
            prev = prev.next
        if head1:
            prev.next = head1
        elif head2:
            prev.next = head2
        return fh.next

def print_list(head):
    cur = head
    out = []
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" ".join(out))


if __name__ == '__main__':
    list1 = ListNode(4)
    list1.next = ListNode(2)
    list1.next.next = ListNode(1)
    list1.next.next.next = ListNode(3)
    out = Solution().sortList(list1)
    print_list(out)

