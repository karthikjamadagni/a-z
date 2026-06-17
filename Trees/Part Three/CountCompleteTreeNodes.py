# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        lsbh = self.getHeight(root.left)
        rsbh = self.getHeight(root.right)

        # If left subtree height == right subtree height
        # Left subtree is a perfect binary tree
        if lsbh == rsbh:
            return (1 << lsbh) + self.countNodes(root.right)

        # Otherwise right subtree is perfect (height = rsbh)
        else:
            return (1 << rsbh) + self.countNodes(root.left)

    def getHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height