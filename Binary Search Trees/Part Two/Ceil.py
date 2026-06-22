'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        temp = root
        ceil = float('inf')
        while temp:
            if temp.data >= x:
                ceil = temp.data
                temp = temp.left
                
            else:
                temp = temp.right
                
                
        return ceil if ceil != float('inf') else -1