# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# key idea:
#  meet at loop length, i.e.,
#     - loop_length = pre + delta
#     - walk the rest of pre -> meet at pre

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
