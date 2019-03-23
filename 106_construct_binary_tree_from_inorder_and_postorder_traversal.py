class Solution(object):
    def __init__(self):
        self.post_idx = -1
    
    def recur_tree(self, l_in, r_in, postorder, inorder, pos):
        if l_in > r_in:
            return None
        v = postorder[self.post_idx]
        self.post_idx -= 1
        cur_node = TreeNode(v)
        j = pos[v]
        cur_node.right = self.recur_tree(j + 1, r_in, postorder, inorder, pos)
        cur_node.left = self.recur_tree(l_in, j - 1, postorder, inorder, pos)
        return cur_node
    
    def buildTree(self, inorder, postorder):
        pos = {v:i for i,v in enumerate(inorder)}
        self.post_idx = len(postorder) - 1
        ret = self.recur_tree(0, len(inorder) - 1, postorder, inorder, pos)
        self.idx_pre = -1 
        return ret 
