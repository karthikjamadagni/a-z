# Structure of linked list Node
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.head = None
        self.top = None
        self.Stacksize = 0
        

    def isEmpty(self):
        # Check if the stack is empty
        if not self.head:
            return True
        else:
            return False
        

    def push(self, x):
        # Adds element x to the top of the stack
        if not self.head:
            self.head = Node(x)
            self.top = self.head
        else:
            new = Node(x)
            self.top.next = new
            self.top = new
        self.Stacksize += 1
        

    def pop(self):
        # Removes an element from the top of the stack
        if not self.isEmpty():
            if not self.head.next:
                ele = self.head.data
                self.head = None
                self.top = None
                self.Stacksize -= 1
                return ele
            else:
                temp = self.head
                prev = None
                while temp.next:
                    prev = temp
                    temp = temp.next
                    
                ele = temp.data
                prev.next = None
                self.top = prev
                self.Stacksize -= 1
                return ele
                
        else:
            return -1
                


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if not self.isEmpty():
            return self.top.data
            
        else:
            return -1


    def size(self):
        # Returns the current size of the stack
        return self.Stacksize