# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        curr = headRef
        while curr:
            nxt = curr.next
            
            while nxt and nxt.data == curr.data:
                curr.next = nxt.next
                nxt = nxt.next
                
            curr = curr.next
            
        return headRef
       