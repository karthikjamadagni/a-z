# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.k = k

        self.inorder(root)

        return self.ans.val if self.ans is not None else -1

    def inorder(self, root):
        if root is None or self.ans is not None:
            return

        self.inorder(root.left)

        self.k -= 1

        if self.k == 0:
            self.ans = root

        self.inorder(root.right)


    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        self.result = [-1]
        self.inorder(root)

        if k > len(self.result):
            return 0

        else:
            return self.result[k]

    
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)