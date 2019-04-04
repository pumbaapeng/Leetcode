# Key idea:
#   split the iterative version of 94_binary-tree-inorder-traversal.py
#     - the initialization becomes __init__
#     - the if_branch moves to has_next()
#     - the else_branch moves to next()


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cur_node = root
        self.s = []

    def hasNext(self) -> bool:
        while self.cur_node or len(self.s) > 0:
            if self.cur_node:
                self.s.append(self.cur_node)
                self.cur_node = self.cur_node.left
            else:
                return True
        return False

    def next(self) -> int:
        if not self.hasNext():
            return -1  # should never happen
        out = self.s.pop()
        self.cur_node = out.right
        return out.val
