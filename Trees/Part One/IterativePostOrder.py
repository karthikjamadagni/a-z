class Solution:
    def iterativePostorder(self, root):
        if root is None:
            return []

        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        result = []

        while stack2:
            result.append(stack2.pop().val)

        return result