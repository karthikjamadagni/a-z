# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        self.index = 0
        return self.builder(preorder, float("inf"))

    def builder(self, preorder: List[int], bound: float) -> Optional[TreeNode] :
        if (self.index > len(preorder)-1) or preorder[self.index] > bound: 
            return None

        new_node = TreeNode(preorder[self.index])
        self.index += 1

        new_node.left = self.builder(preorder, new_node.val)
        new_node.right = self.builder(preorder, bound)

        return new_node


        