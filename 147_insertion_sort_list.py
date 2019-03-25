class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head # at least 2 nodes
        fh = ListNode(-1)
        fh.next = head
        last_sorted, replace = head, head.next
        while replace:
            next_replace = replace.next
            ins = fh
            while ins.next != replace and replace.val > ins.next.val:
                ins = ins.next
            if ins.next == replace:
                last_sorted = last_sorted.next
            else:
                replace.next = ins.next
                ins.next = replace
            replace = next_replace
            last_sorted.next = next_replace
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
    out = Solution().insertionSortList(list1)
    print_list(out)
