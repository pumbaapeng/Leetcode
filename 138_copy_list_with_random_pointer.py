class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        # make zigzag
        cur_node = head
        while cur_node:
            new_node = Node(cur_node.val, cur_node.next, None)
            cur_node.next = new_node
            cur_node = new_node.next
        # make random edges and restore edges
        cur_node = head
        while cur_node:
            cur_node.next.random = cur_node.random.next if cur_node.random else None
            cur_node = cur_node.next.next
        new_head = head.next if head else None
        cur_node = head
        while cur_node:
            next_node = cur_node.next.next
            cur_node.next.next = next_node.next if next_node else None
            cur_node.next = next_node
            cur_node = next_node
        return new_head

def print_ll(head) :
    cur = head
    while cur:
        print "val = %d, next = %d, rdn = %d" % (cur.val, cur.next.val if cur.next else -1, cur.random.val if cur.random else -1)
        cur = cur.next

node1 = Node(1, None, None)
node2 = Node(2, None, None)
node1.next = node2
node1.random = node2
node2.random = node2

ret = Solution().copyRandomList(node1)

print_ll(node1)
print_ll(ret)


