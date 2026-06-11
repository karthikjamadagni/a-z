class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')
        

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal, val)
        self.stack.append((val, self.minVal))


    def pop(self) -> None:
        if not self.stack:
            return -1
        else:
            val, minValue = self.stack.pop()
            if not self.stack:
                self.minVal = float('inf')
            else:
                ele, value = self.stack[-1]
                self.minVal = value
            return val
        

    def top(self) -> int:
        if not self.stack:
            return -1
        else:
            val, minValue = self.stack[-1]
            return val

    def getMin(self) -> int:
        if not self.stack:
            return -1
        else:
            val, minValue = self.stack[-1]
            return minValue
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()