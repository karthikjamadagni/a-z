'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def merge(self, root1, root2):
        # code here
        self.temp = []
        self.inorder(root1)
        first_list = self.temp.copy()
        self.temp = []
        self.inorder(root2)
        second_list = self.temp.copy()
        ans = []
        
        i, j = 0, 0
        while i < len(first_list) and j < len(second_list):
            if first_list[i] <= second_list[j]:
                ans.append(first_list[i])
                i += 1
                
            else:
                ans.append(second_list[j])
                j += 1
                
        while i < len(first_list):
            ans.append(first_list[i])
            i += 1
            
        while j < len(second_list):
            ans.append(second_list[j])
            j += 1
            
        return ans
        
        
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        self.temp.append(root.data)
        self.inorder(root.right)
        
    
        