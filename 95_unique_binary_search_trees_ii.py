# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.get_tree(1, n)
    def get_tree(self, l, r):
        ret = []
        if l > r:
            return [None]
        for c in range(l, r + 1):
            left_options = self.get_tree(l, c - 1)
            right_options = self.get_tree(c + 1, r)
            for left_head in left_options:
                for right_head in right_options:
                    c_node = TreeNode(c)
                    c_node.left = left_head
                    c_node.right = right_head
                    ret.append(c_node)
        return ret
