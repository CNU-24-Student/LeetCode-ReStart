class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []
        
    def push(self,value:int) -> None:
        self.stk.append(value)
        if len(self.minStk) == 0:
            self.minStk.append(value)
        else:
            self.minStk.append(min(self.minStk[-1],value))

    def pop(self) -> None:
        self.stk = self.stk[:-1]
        self.minStk = self.minStk[:-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()