# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:

    def distanceKFinder(self, root: TreeNode, distance):

        if root is None:
            return
        if root in self.visited:
            return

        if distance == 0:
            self.answer.append(root.val)

        self.visited.add(root)

        self.distanceKFinder(root.left, distance-1)
        self.distanceKFinder(root.right, distance-1)
        self.distanceKFinder(self.parent_map.get(root), distance-1)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent_map = {}
        dq = deque([root])

        while dq:
            front = dq.popleft()
            if front.left:
                dq.append(front.left)
                self.parent_map[front.left] = front

            if front.right: 
                dq.append(front.right)
                self.parent_map[front.right] = front

        self.visited = set()

        self.answer = []
        self.distanceKFinder(target, k)

        return self.answer

    