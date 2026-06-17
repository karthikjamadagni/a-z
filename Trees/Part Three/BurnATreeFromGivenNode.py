'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    def minTime(self, root, target):
        # code here
        if root is None:
            return 0
            
        parent_map = {}
        parent_map[root] = None
        dq = deque([root])
        target_node = None
        
        while dq:
            front = dq.popleft()
            if front.data == target:
                target_node = front
            if front.left:
                dq.append(front.left)
                parent_map[front.left] = front
                
            if front.right:
                dq.append(front.right)
                parent_map[front.right] = front
                
        visited = set()
        visited.add(target_node)
        
        dq = deque([target_node])
        time_required = 0
        
        while dq:
            size = len(dq)
            burned = False
            
            for _ in range(size):
                front = dq.popleft()
                
                if front.left and front.left not in visited:
                    dq.append(front.left)
                    visited.add(front.left)
                    burned = True
                    
                if front.right and front.right not in visited:
                    dq.append(front.right)
                    visited.add(front.right)
                    burned = True
                    
                if parent_map[front] and parent_map[front] not in visited:
                    dq.append(parent_map[front])
                    visited.add(parent_map[front])
                    burned = True
                    
            if burned:
                time_required += 1
                
        return time_required
        
        
