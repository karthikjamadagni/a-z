'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        temp = root
        
        floor = float('-inf')
        
        while temp:
            if temp.data <= k:
                floor = temp.data
                temp = temp.right
                
            else:
                temp = temp.left
                
        return floor if floor != float('-inf') else -1