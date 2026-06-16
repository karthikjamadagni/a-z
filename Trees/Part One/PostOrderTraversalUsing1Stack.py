# https://chatgpt.com/s/t_69996368d7fc819197f4893a75bea74f

from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        postorder = []
        last_visited = None
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left  # go as left as possible
            else:
                peek_node = stack[-1]
                # if right child exists and not processed yet
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    postorder.append(peek_node.val)
                    last_visited = stack.pop()

        return postorder