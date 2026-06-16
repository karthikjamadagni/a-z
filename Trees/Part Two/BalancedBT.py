# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.helper(root) != -1


    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.helper(root.left)
        if left == -1:
            return -1

        right = self.helper(root.right)
        if right == -1:
            return -1


        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)



        

# IDK why a heightchecker function is there in the notes
def heightChecker(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.heightChecker(root.left)
        if left == -1:
            return -1

        right = self.heightChecker(root.right)
        if right == -1:
            return -1


        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

# This is the function to check height