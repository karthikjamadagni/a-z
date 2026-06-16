# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columndict = defaultdict(list)
        dq = deque([(root, 0, 0)])

        while dq:
            node, row, col = dq.popleft()
            columndict[col].append((row, node.val))


            if node.left:
                dq.append((node.left, row+1, col-1))

            if node.right:
                dq.append((node.right, row+1, col+1))

        answer = []

        print(columndict)

        for i in sorted(columndict.keys()):
            column = columndict[i]
            column.sort()

            new_list = []

            for pair in column:
                val = pair[1]
                new_list.append(val)

            answer.append(new_list)

        return answer

        

        
        