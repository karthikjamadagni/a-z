class Solution:
    def iterativeInorder(self, root):
        stack = []
        curr = root
        result = []

        while curr is not None or stack:

            # Go as left as possible
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # Process node
            curr = stack.pop()
            result.append(curr.val)

            # Move to right subtree
            curr = curr.right

        return result