class Solution:
    def inprepost(self, root):
        stack = []
        inorder = []
        preorder = []
        postorder = []
        if root is None:
            return [inorder, preorder, postorder]
        stack.append((root, 1))
        
        while stack:
            node, state = stack[-1]
            stack.pop()
            if state == 1:
                preorder.append(node.val)
                nextState = state + 1
                stack.append((node, nextState))
                if node.left != None:
                    stack.append((node.left, 1))
                    
            elif state == 2:
                inorder.append(node.val)
                nextState = state + 1
                stack.append((node, nextState))
                if node.right != None:
                    stack.append((node.right, 1))
                    
            else:
                postorder.append(node.val)
                
        return [inorder, preorder, postorder]