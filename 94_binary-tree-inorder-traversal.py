# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative solution
# Idea:
# 1) use (cur_node, stack)
# 2) when cur_node is valid, push it and go left
# 3) when cur_node is not valid, pop it, output, and go right
class Solution(object):
    def inorderTraversal(self, root):
        cur_node = root
        stack = []
        ret = []
        while cur_node or len(stack) > 0:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                ret.append(cur_node.val)
                cur_node = cur_node.right
        return ret

# recursive solution
class Solution(object):
    def inorderTraversal(self, root):
        def recur(cur_node, ret):
            if cur_node == None:
                return
            recur(cur_node.left, ret)
            ret.append(cur_node.val)
            recur(cur_node.right, ret)
            return
        ret = []
        recur(root, ret)
        return ret
        
