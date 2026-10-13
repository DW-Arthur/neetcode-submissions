class MinStack:

    def __init__(self):
        # Brute force
        self.arr =[]
    def push(self, val: int) -> None:
        self.arr.append(val)
    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]
    def getMin(self) -> int:
        # Use a tmp array
        # Keep popping the stack and store it in the tmp
        # keep track of min
        # Add the value of tmp back in the stack to keep order
        tmp = []
        mini = self.arr[-1]
        while self.arr:
            mini = min(mini,self.arr[-1])
            tmp.append(self.arr.pop())
        while tmp:
            self.arr.append(tmp.pop())
        return mini
