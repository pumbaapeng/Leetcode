from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        q = deque()
        q.append(root)
        ret = []
        count = 1
        cur_level = []
        while len(q) > 0:
            cur_node = q.popleft()
            cur_level.append(cur_node.val)
            count -= 1
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            if count == 0:
                count = len(q)
                ret.append(cur_level)
                cur_level = []
        for i, l in enumerate(ret):
            if i % 2 == 1:
                ret[i] = l[::-1]
        return ret
