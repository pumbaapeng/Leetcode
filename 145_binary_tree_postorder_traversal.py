class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            cur_node = stack.pop()
            ret.append(cur_node.val)
            if cur_node.left:  # note here
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return ret[::-1]
