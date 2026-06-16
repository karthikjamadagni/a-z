# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.diameter = 0

        self.diameterFinder(root)

        return self.diameter

    def diameterFinder(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftHeight = self.diameterFinder(root.left)
        rightHeight = self.diameterFinder(root.right)

        self.diameter = max(self.diameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)

    
        