# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.maximumDepth = 1
        if(root.left):
            self.helper(root.left, 1)

        if(root.right):
            self.helper(root.right, 1)

        return self.maximumDepth


    def helper(self, root: Optional[TreeNode], depth) -> None:
        if root is None:
            return

        depth += 1
        self.maximumDepth = max(self.maximumDepth, depth)
        self.helper(root.left, depth)
        self.helper(root.right, depth)


        
        