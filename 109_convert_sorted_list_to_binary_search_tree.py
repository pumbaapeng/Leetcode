# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def recur(head, end):
            if head == end:
                return None
            elif head.next == end:
                return TreeNode(head.val)
            mid, right = head, head.next
            while right != end and right.next != end:
                right = right.next.next
                mid = mid.next
            cur = TreeNode(mid.val)
            cur.left = recur(head, mid)
            cur.right = recur(mid.next, end)
            return cur
        return recur(head, None)