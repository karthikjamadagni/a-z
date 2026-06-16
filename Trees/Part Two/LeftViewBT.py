# leftview:
''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque, defaultdict
class Solution:
    def leftView(self, root):
        # code here
        if root is None:
            return []
        sm_map = []
        dq = deque([root])
        answer = []
        
        while dq:
            length = len(dq)
            
            for i in range(length):
                node = dq.popleft()
                if i == 0:
                    answer.append(node.data)
                    
                if node.left:
                    dq.append(node.left)
                    
                if node.right:
                    dq.append(node.right)
                    
        return answer