'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def sum_property_checker(self, root):
        if root is None:
            return True
            
        if root.left is None and root.right is None:
            return True
            
        leftval = root.left.data if root.left else 0
        rightval = root.right.data if root.right else 0
        
        cursum = leftval + rightval
        
        return (
        (root.data == cursum) and
        self.sum_property_checker(root.left) and
        self.sum_property_checker(root.right)
        )
        
        
    
    
    def isSumProperty(self, root):
        # code here
        if root is None:
            return True
            
        return self.sum_property_checker(root)
        
        