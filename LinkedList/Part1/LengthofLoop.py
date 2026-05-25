'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        fast, slow = head, head
        count = 0
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                
                count += 1
                
                temp = slow.next
                
                while slow != temp:
                    temp = temp.next
                    count += 1
                    
                return count
                
        return 0