# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def symmetricFinder(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True

        elif not left or not right:
            return False

        return left.val == right.val and self.symmetricFinder(left.left, right.right) and self.symmetricFinder(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.symmetricFinder(root.left, root.right)