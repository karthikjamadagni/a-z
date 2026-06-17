class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        self.index_map = {value: idx for idx, value in enumerate(inorder)}

        return self.helper(preorder, 0, len(preorder)-1,
                           inorder, 0, len(inorder)-1)

    def helper(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None

        root_val = preorder[preStart]
        root = TreeNode(root_val)

        inRoot = self.index_map[root_val]
        nums_left = inRoot - inStart

        root.left = self.helper(preorder,
                                preStart + 1,
                                preStart + nums_left,
                                inorder,
                                inStart,
                                inRoot - 1)

        root.right = self.helper(preorder,
                                 preStart + nums_left + 1,
                                 preEnd,
                                 inorder,
                                 inRoot + 1,
                                 inEnd)

        return root