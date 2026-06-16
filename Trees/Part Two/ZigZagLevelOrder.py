from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        dq = deque([root])
        left_to_right = True

        while dq:
            level_nodes = []
            length = len(dq)

            for _ in range(length):
                if left_to_right:
                    node = dq.popleft()
                    level_nodes.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                else:
                    node = dq.pop()
                    level_nodes.append(node.val)
                    # Append children in reverse order for next level
                    if node.right:
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)

            ans.append(level_nodes)
            left_to_right = not left_to_right

        return ans