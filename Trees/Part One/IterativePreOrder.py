class Solution:
    def iterativepreorder(self, root):
        if root is None:
            return []
        stack = []
        stack.append(root)
        lst = []
        
        while stack:
            node = stack[-1]
            stack.pop()
            lst.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
                
        return lst