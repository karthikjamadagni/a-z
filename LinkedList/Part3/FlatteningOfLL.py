# class Node:
#     def __init__(self, d):
#         self.data = d
#         self.next = None
#         self.bottom = None


class Solution:
    
    # Merge two sorted bottom-linked lists
    def merge(self, a, b):
        
        # If one list is empty
        if not a:
            return b
        if not b:
            return a
        
        # Choose smaller node and recur
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
        
        # next pointer is not needed in final flattened list
        result.next = None
        
        return result
    
    
    def flatten(self, root):
        
        # Base case
        if not root or not root.next:
            return root
        
        # Recursively flatten the remaining list
        root.next = self.flatten(root.next)
        
        # Merge current list with flattened next lists
        root = self.merge(root, root.next)
        
        return root