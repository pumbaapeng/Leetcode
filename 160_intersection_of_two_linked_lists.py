# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        n_a = self.get_length(headA)
        n_b = self.get_length(headB)
        if n_a > n_b:
            headA, headB = headB, headA  # make headA the shorter one
        diff = abs(n_a - n_b)
        cur_a = headA
        cur_b = headB
        for i in range(diff):
            cur_b = cur_b.next
        while cur_a and cur_b:
            if cur_a == cur_b:
                return cur_a
            cur_a, cur_b = cur_a.next, cur_b.next
        return None

    def get_length(self, head):
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        return cnt

