'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque, defaultdict

class Solution:
    def bottomView(self, root):
        # code here
        if root is None:
            return []
            
        hd_map = defaultdict(int)
        
        answer = []
        
        dq = deque([(root, 0)])
        
        while dq:
            node, hd = dq.popleft()
            
            hd_map[hd] = node.data
            
            if node.left:
                dq.append((node.left, hd-1))
                
            if node.right:
                dq.append((node.right, hd+1))
                
        for key in sorted(hd_map.keys()):
            answer.append(hd_map[key])
        
        return answer
        