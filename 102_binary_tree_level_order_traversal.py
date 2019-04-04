# Solution 1: less memory
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        q = deque()
        if root:
            q.append(root)
            ret.append([root.val])
        to_pop = 1
        while len(q) != 0:
            cur_node = q.popleft()
            to_pop -= 1
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            if to_pop == 0 and len(q) > 0:
                ret.append([v.val for v in q])
                to_pop = len(q)
        return ret


# Solution2: cleaner
from collections import deque

class Solution:
    def levelOrder(self, root):
        ret = []
        q = deque()
        if root:
            q.append((root, 0))
        while len(q) != 0:
            node, lv = q.popleft()
            if lv >= len(ret):
                ret.append([])
            ret[lv].append(node.val)
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))
        return ret
            
