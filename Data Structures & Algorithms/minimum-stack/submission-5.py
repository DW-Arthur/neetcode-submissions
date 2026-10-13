class MinStack:

    def __init__(self):
        #Double stack
        #Have a min stack, normal stack.
        #At each level, the min stack keeps the lowest number
        self.arr =[]
        self.minStack =[]

    def push(self, val: int) -> None:
        # At each push, check the minStack for minimum 
        self.arr.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            mini = min(self.minStack[-1],val)
            self.minStack.append(mini)
    def pop(self) -> None:
        self.minStack.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
