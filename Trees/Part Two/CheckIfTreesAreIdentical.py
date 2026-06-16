from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None
        if not p and not q:
            return True
        # If one is None
        if not p or not q:
            return False

        tree1 = deque([p])
        tree2 = deque([q])

        while tree1 and tree2:
            tree1Node = tree1.popleft()
            tree2Node = tree2.popleft()

            if tree1Node.val != tree2Node.val:
                return False

            # Check left children
            if tree1Node.left and tree2Node.left:
                tree1.append(tree1Node.left)
                tree2.append(tree2Node.left)
            elif tree1Node.left or tree2Node.left:
                return False

            # Check right children
            if tree1Node.right and tree2Node.right:
                tree1.append(tree1Node.right)
                tree2.append(tree2Node.right)
            elif tree1Node.right or tree2Node.right:
                return False

        return not tree1 and not tree2