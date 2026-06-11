class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.stack = [-1] * n
        self.size = 0
        self.top = -1

    
    def isEmpty(self):
        # Check if stack is empty
        if self.size == 0:
            return True
        else:
            return False
            
    
    def isFull(self):
        # Check if stack is full
        if self.stack[-1] == -1:
            return False
            
        else:
            return True

    
    def push(self, x):
        # Insert x at the top of the stack
        if not self.isFull():
            self.top += 1
            self.size += 1
            self.stack[self.top] = x

    
    def pop(self):
        if not self.isEmpty():
            ele = self.stack[self.top]
            self.stack[self.top] = -1   # clear the slot
            self.top -= 1
            self.size -= 1
            return ele
        else:
            return -1

    
    def peek(self):
        # Returns the top element of the stack
        if not self.isEmpty():
            return self.stack[self.top]
            
        else:
            return -1