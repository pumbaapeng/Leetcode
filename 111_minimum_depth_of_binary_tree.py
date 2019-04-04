from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append((root, 0))
        while len(q) != 0:
            node, lv = q.popleft()
            if not node.left and not node.right:
                return lv + 1
            if node.left:
                q.append((node.left, lv + 1)) 
            if node.right:
                q.append((node.right, lv + 1))
        return 0
        
