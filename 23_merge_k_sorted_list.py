import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        heap = []
        fh = ListNode(-1)
        for list_head in lists:
            if list_head:
                heapq.heappush(heap, list_head)
        ins = fh
        while heap:
            node = heapq.heappop(heap)
            if node:
                ins.next = node
                ins = ins.next
                if node.next:
                    heapq.heappush(heap, node.next)
        return fh.next

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = ListNode(2)
list3.next = ListNode(6)
ipt = [list1, list2, list3]
out = Solution().mergeKLists(ipt)


def print_list(head):
    cur = head
    out = []
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" ".join(out))


print_list(out)
