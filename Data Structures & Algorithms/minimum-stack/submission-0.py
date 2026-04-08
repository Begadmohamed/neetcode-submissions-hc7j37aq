class MinStack:

    def __init__(self):
        self.items=[]
        self.minStack=[]
    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minStack or val<=self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.items:
            self.items.pop()
            self.minStack.pop()


    def top(self) -> int:
        if self.items:
            return self.items[-1]
        return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None
        
