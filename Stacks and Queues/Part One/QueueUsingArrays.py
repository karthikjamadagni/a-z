class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.q = [None] * n
        self.size = n
        self.rear = -1
        self.front = -1

    
    def isEmpty(self):
        # Check if queue is empty
        if self.front == -1:
            return True
        else:
            return False
    
    def isFull(self):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            return True
            
        else:
            return False

    
    def enqueue(self, x):
        # Enqueue
        if self.isFull():
            return False
            
        else:
            if self.front == -1:
                self.front = 0
                
            self.rear += 1
            self.q[self.rear] = x
            return True
            

    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return -1
            
        else:
            ele = self.q[self.front]
            self.front = (self.front + 1) % self.size
            
            if self.front == self.rear:
                self.front = self.rear = -1
                
            return ele

    
    def getFront(self):
        # Get front element
        if not self.isEmpty():
            return self.q[self.front]
            
        else:
            return -1
       
    
    def getRear(self):
        # Get rear element 
        if not self.isFull():
            return self.q[self.rear]
        else:
            return -1
        
        