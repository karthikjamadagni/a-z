# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        self.indexes_map = {}

        for i in range(len(inorder)):
            self.indexes_map[inorder[i]] = i

        root = self.treeBuilder(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

        return root

    def treeBuilder(self, inorder, instart, inend, postorder, poststart, postend):
        if instart > inend or poststart > postend:
            return None

        root = TreeNode(postorder[postend])
        inroot = self.indexes_map[postorder[postend]]
        nums_left = inroot - instart

        root.left = self.treeBuilder(inorder, instart, inroot-1, postorder, poststart, poststart + nums_left-1)

        root.right = self.treeBuilder(inorder, inroot+1, inend, postorder, poststart + nums_left, postend-1)

        return root
        