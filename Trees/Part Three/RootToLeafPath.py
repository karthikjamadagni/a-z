from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    
    def path_printer(self, root, temp_list) -> None:
        if root is None:
            return
            
        temp_list.append(root.data)
        
        if root.left is None and root.right is None:
            self.answer.append(temp_list.copy())
            
        else:
            self.path_printer(root.left, temp_list)
            self.path_printer(root.right, temp_list)
            
        temp_list.pop()
        
        
        
    def Paths(self, root):
        # code here
        if root is None:
            return []
        self.answer = []
        temp_list = []
        
        self.path_printer(root, temp_list)
        return self.answer
                