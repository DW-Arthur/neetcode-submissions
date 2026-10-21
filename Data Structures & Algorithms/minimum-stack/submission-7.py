class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # How to append minStack
        # The minStack and stack should have the same length
        # If the about to be added value is less than the minStack top, append it
        # If the about to be added value is more than minStack top, copy the minStack
        # top value and add it again
        if len(self.minStack) == 0:
            self.minStack.append(val)
            return
        if val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
