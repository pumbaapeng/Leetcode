"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {}
        return Solution.get_clone(node, cloned)
    
    @staticmethod
    def get_clone(node, cloned):
        if id(node) in cloned:
            return cloned[id(node)]
        cur_clone = Node(node.val, [])
        cloned[id(node)] = cur_clone
        for nb in node.neighbors:
            cur_clone.neighbors.append(Solution.get_clone(nb, cloned))
        return cur_clone
