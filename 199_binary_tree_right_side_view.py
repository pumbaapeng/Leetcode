# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ret = []
        q = deque()
        to_pop = 0
        if root:
            q.append(root)
            to_pop = 1
        while len(q) != 0:
            cur_node = q.popleft()
            to_pop -= 1
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            if to_pop == 0:
                ret.append(cur_node.val)
                to_pop = len(q)
        return ret
            
        
