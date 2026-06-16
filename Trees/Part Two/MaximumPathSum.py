# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.maximumSum = root.val

        self.maximumSumFinder(root, root.val)


        return self.maximumSum


    def maximumSumFinder(self, root: Optional[TreeNode], curSum: int) -> int:
        if root is None:
            return 0

        leftSubTreeSum = max(self.maximumSumFinder(root.left, 0), 0)

        rightSubTreeSum = max(self.maximumSumFinder(root.right, 0), 0)

        currentPathSum = leftSubTreeSum + rightSubTreeSum + root.val

        self.maximumSum = max(self.maximumSum, currentPathSum)

        return root.val + max(leftSubTreeSum, rightSubTreeSum)