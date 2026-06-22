"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        # code here
        prev = None
        while root:
            prev = root
            root = root.left
            
        return prev.data
        