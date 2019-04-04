# recursive solution
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return Solution.is_mirror(root.left, root.right)
    @staticmethod
    def is_mirror(h1, h2):
        if not h1 and not h2:
            return True
        if not h1 or not h2:
            return False
        return h1.val == h2.val and Solution.is_mirror(h1.left, h2.right) and Solution.is_mirror(h1.right, h2.left)


# BFS solution
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = deque()
        push_idx = 0
        q.appendleft((root, push_idx))
        cnt = 1
        next_check_size = 2
        while len(q) != 0:
            cur, j = q.pop()
            cnt -= 1
            if cnt == 0:
                push_idx = 0
            if cur.left:
                q.appendleft((cur.left, push_idx))
            push_idx += 1
            if cur.right:
                q.appendleft((cur.right, push_idx))
            push_idx += 1
            if cnt == 0:
                if not Solution.check_symmetry(q, next_check_size):
                    return False
                next_check_size *= 2
        return True

    @staticmethod
    def check_symmetry(q, next_check_size):
        l = len(q)
        if l % 2 != 0:
            return False
        stack = []
        for i in range(l // 2):
            stack.append(q[i])
        for i in range(1 // 2, l):
            node, idx = stack.pop()
            node1, idx1 = q[i]
            if node.val != node1.val or idx + idx1 != next_check_size - 1:
                return False
        return True


if __name__ == '__main__':
    ipt = [1,2,2,3,4,4,3]
    print(Solution().isSymmetric(ipt))
