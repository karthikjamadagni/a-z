"""Structure of a linked list node

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
class Solution:

    def deleteAllOccurances(self, head, x):
        # Code Here
        if not head:
            return None
            
        prev = None
        temp = head
        
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                    temp = temp.next
                
                else:
                    head = head.next
                    temp = temp.next
                    
            else:
                prev = temp
                temp = temp.next
                
                
        return head
                
        