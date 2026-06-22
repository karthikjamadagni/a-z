# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validator(node, low=float('-inf'), high = float('inf')):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return validator(node.left, low, node.val) and validator(node.right, node.val, high)

        return validator(root)