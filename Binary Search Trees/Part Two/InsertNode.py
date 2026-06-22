# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        newNode = TreeNode(val)

        temp = root

        while temp:
            if temp.val < val:
                if temp.right:
                    temp = temp.right

                else:
                    temp.right = newNode
                    break

            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = newNode
                    break

        return root