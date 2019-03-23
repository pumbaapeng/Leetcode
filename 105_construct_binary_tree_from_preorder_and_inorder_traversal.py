class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.idx_pre = 0

    def recur_tree(self, l_in, r_in, preorder, inorder, pos):
        if l_in > r_in:
            return None
        v = preorder[self.idx_pre]
        self.idx_pre += 1
        cur_node = TreeNode(v)
        j = pos[v]
        cur_node.left = self.recur_tree(l_in, j - 1, preorder, inorder, pos)
        cur_node.right = self.recur_tree(j + 1, r_in, preorder, inorder, pos)
        return cur_node

    def buildTree(self, preorder, inorder):
        pos = {v:i for i,v in enumerate(inorder)}
        self.idx_pre = 0
        ret = self.recur_tree(0, len(inorder) - 1, preorder, inorder, pos)
        self.idx_pre = 0
        return ret

if __name__ == "__main__":
    tree = Solution().buildTree([1, 2], [1, 2])
    assert tree.val == 1
    assert tree.right.val == 2
    tree = Solution().buildTree([1, 2, 3], [1, 2, 3])
    assert tree.val == 1
    assert tree.right.val == 2
    assert tree.right.right.val == 3
    tree = Solution().buildTree([1, 2], [1, 2])
    assert tree.val == 1
    assert tree.right.val == 2
    tree = Solution().buildTree([1, 2, 3], [1, 2, 3])
    assert tree.val == 1
    assert tree.right.val == 2
    assert tree.right.right.val == 3 
