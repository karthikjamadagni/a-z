# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #simple enik beku gandu morris traversal madu
        # if root is None:
        #     return []

        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        if root is None:
            return []

        answer = []
        curr = root
        while curr:
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right

            else:
                prev = curr.left

                while prev.right != None and prev.right != curr:
                    prev = prev.right

                

                if not prev.right:
                    prev.right = curr
                    curr = curr.left

                else:
                    prev.right = None
                    answer.append(curr.val)
                    curr = curr.right


        return answer



        