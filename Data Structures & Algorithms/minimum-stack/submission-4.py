class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
               self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # O(n)
        # return min(self.stack[0 : len(self.stack)]) 
        # O(1)
        return self.minStack[-1]
