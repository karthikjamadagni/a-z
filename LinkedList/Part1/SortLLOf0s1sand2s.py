'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        zeroDummy = Node(-1)
        oneDummy = Node(-1)
        twoDummy = Node(-1)
        
        zero = zeroDummy
        one = oneDummy
        two = twoDummy
        
        temp = head
        
        while temp:
            nxt = temp.next
            if temp.data == 0:
                zero.next = temp
                temp.next = None
                zero = zero.next
                
            elif temp.data == 1:
                one.next = temp
                temp.next = None
                one = one.next
                
            else:
                two.next = temp
                temp.next = None
                two = two.next
                
            temp = nxt
            
        zero.next = oneDummy.next if oneDummy.next else twoDummy.next
        one.next = twoDummy.next

        return zeroDummy.next
                