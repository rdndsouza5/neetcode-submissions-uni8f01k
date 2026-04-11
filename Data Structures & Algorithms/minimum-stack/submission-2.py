class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = val
        if self.stack:
            val22, minVal = self.stack[-1]
        minVal = min(val, minVal)
        self.stack.append((val, minVal))

    def pop(self) -> None:
        print(self.stack)
        self.stack.pop()
        

    def top(self) -> int:
        val, minval = self.stack[-1]    
        return val    

    def getMin(self) -> int:
        val, minval = self.stack[-1]    
        return minval
