class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reverse = {']': '[', ')':'(', '}':'{'}
        if len(s) ==1:
            return False
        for i in s:
            if i in reverse:
                if len(stack) ==0:
                    return False
                test = stack.pop()
                if test != reverse[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) ==0
        