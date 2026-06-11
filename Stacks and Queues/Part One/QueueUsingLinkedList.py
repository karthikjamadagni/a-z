# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.front = None
        self.rear = None
        self.qSize = 0
        

    def isEmpty(self):
        # Return True if queue is empty, else False
        if not self.front:
            return True
            
        else:
            return False
        

    def enqueue(self, x):
        # Add element x to the rear
        if not self.front:
            self.front = Node(x)
            self.rear = self.front
        else:
            new = Node(x)
            self.rear.next = new
            self.rear = new
            
        self.qSize += 1
        

    def dequeue(self):
        # Remove the front element
        if not self.isEmpty():
            if self.front == self.rear:
                ele = self.front.data
                self.front = self.rear = None
                self.qSize -= 1
                return ele
                
            else:
                ele = self.front.data
                self.front = self.front.next
                self.qSize -= 1
                return ele
                


    def getFront(self):
        # Return front element
        # return -1 if empty
        if not self.isEmpty():
            return self.front.data
        else:
            return -1


    def size(self):
        # Return current size
        return self.qSize
