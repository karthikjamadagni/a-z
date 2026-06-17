# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = ""
        dq = deque([root])

        

        if root is None:
            return ""

        string += str(root.val)
        string += ','

        while dq:
            front = dq.popleft()

            if front.left:
                dq.append(front.left)
                string += str(front.left.val)

            else:
                string += '#'

            string += ','


            if front.right:
                dq.append(front.right)
                string += str(front.right.val)

            else:
                string += '#'

            string += ','

        print(string)
        return string[:len(string)-1]

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data_list = data.split(',')
        root = TreeNode(data_list[0])
        dq = deque([root])

        j = 1

        while j < len(data_list):
            front = dq.popleft()

            front.left = TreeNode(int(data_list[j])) if data_list[j] != '#' else None
            if front.left:
                dq.append(front.left)

            front.right = TreeNode(int(data_list[j+1])) if data_list[j+1] != '#' else None
            if front.right:
                dq.append(front.right)

            j += 2



        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))