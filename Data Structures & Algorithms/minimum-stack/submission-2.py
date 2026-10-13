class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        return self.arr.append(val)

    def pop(self) -> None:
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        # Brute force solution
        # use a min function to get the min
        # make a tmp function to add all the popped arr into 
        mini = self.arr[-1]
        tmp = []
        while self.arr:
            mini = min(mini, self.arr[-1])
            tmp.append(self.arr.pop())
        while tmp:
            self.arr.append(tmp.pop())
        return mini


