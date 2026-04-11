class MinStack:
    a =[]
    def __init__(self):
        self.a=[]

    def push(self, val: int) -> None:
        self.a.append(val)

    def pop(self) -> None:
        self.a.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.a[-1]

        while len(self.a):
            mini = min(mini, self.a[-1])
            tmp.append(self.a.pop())
        
        while len(tmp):
            self.a.append(tmp.pop())
        
        return mini