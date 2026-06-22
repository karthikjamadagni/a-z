# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self.helper(root)

        dummy = root

        while root:

            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break

                else:
                    root = root.left

            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return dummy

    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left == None:
            return root.right

        elif root.right == None:
            return root.left

        else:
            rightChild = root.right
            lastRightChild = self.findLastRightChild(root.left)
            lastRightChild.right = rightChild
            return root.left

    def findLastRightChild(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.right is None:
            return root

        return self.findLastRightChild(root.right)

        
