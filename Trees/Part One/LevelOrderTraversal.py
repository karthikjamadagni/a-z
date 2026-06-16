# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        q = deque()
        q.append(root)
        ans = []

        while q:
            level_nodes = []
            level = len(q)

            for i in range(level):
                node = q.popleft()
                level_nodes.append(node.val)
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            ans.append(level_nodes)


        return ans