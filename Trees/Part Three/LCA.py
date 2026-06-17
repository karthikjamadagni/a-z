# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowest_common_ancestor_finder(self, node, p, q):
        if node is None:
            return None

        if node == p:
            return p

        elif node == q:
            return q

        a = self.lowest_common_ancestor_finder(node.left, p, q) 
        b = self.lowest_common_ancestor_finder(node.right, p, q)

        if a is not None and b is not None:
            return node

        return a if a is not None else b
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        answer = self.lowest_common_ancestor_finder(root, p, q)

        return answer


    

        