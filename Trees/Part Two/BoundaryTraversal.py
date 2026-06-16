'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    
    def is_leaf_node(self, node):
        if node is None:
            return False
            
        return node and not node.left and not node.right
    
    def add_left_boundary(self, root):
        curr = root.left
        while curr:
            if not self.is_leaf_node(curr):
                self.answer.append(curr.data)
                
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
                    
                    
    def add_leaf_nodes(self, root):
        if root is None:
            return
        
        if self.is_leaf_node(root):
            self.answer.append(root.data)
            return
        
        self.add_leaf_nodes(root.left)
        self.add_leaf_nodes(root.right)
        
    def add_right_boundary(self, root):
        curr = root.right
        stack = [] # just to reverse it that's it
        
        while curr:
            if not self.is_leaf_node(curr):
                stack.append(curr.data)
                
            if curr.right:
                curr = curr.right
                
            else:
                curr = curr.left
                
        while stack:
            self.answer.append(stack.pop())
                
            
    
    def boundaryTraversal(self, root):
        # code here
        if root is None:
            return []
        self.answer = []
        if not self.is_leaf_node(root):
            self.answer.append(root.data)
        self.add_left_boundary(root)
        self.add_leaf_nodes(root)
        self.add_right_boundary(root)
        return self.answer
        
        
        