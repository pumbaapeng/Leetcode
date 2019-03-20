class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        headNode = lastNode = None
        while l1 or l2 or carry :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = carry + val1 + val2
            curNode = ListNode(val % 10)
            carry = val / 10
            if lastNode == None :
                lastNode = headNode = curNode
            else :
                lastNode.next = curNode
            lastNode = curNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return headNode

# remember to use a fake-head
if __name__ == "__main__":
    class Solution():
        def addTwoNumbers(self, l1, l2):
            carry = 0
            fh = last = ListNode(-1)
            while l1 or l2 or carry:
                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0
                val = carry + val1 + val2
                cur, carry = ListNode(val % 10), val / 10
                last.next = cur
                last = cur
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            return fh.next
    
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = Solution().addTwoNumbers(l1, l2)
    print res.val
    assert res.val == 7, str(res.val)
    print res.next.val
    assert res.next.val == 0
    assert res.next.next.val == 8
    l1 = ListNode(5)
    l2 = ListNode(5)
    res = Solution().addTwoNumbers(l1, l2)
    assert res.val == 0
    assert res.next.val == 1
