'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque, defaultdict

class Solution:
    def topView(self, root):
        # code here
        map = defaultdict(int)
        if root is None:
            return []
            
        dq = deque([(root, 0)])
        answer = []
        
        while dq:
            node, hd = dq.popleft()
            
            if hd not in map:
                map[hd] = node.data
                
            if node.left:
                dq.append((node.left, hd-1))
                
            if node.right:
                dq.append((node.right, hd+1))
                
        for key in sorted(map.keys()):
            answer.append(map[key])
            
        return answer
            
        
        