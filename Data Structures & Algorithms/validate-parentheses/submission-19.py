class Solution:
    def isValid(self, s: str) -> bool:
        #once meet a cloing bracket, pop the stack, see if it matches
        # This will fail
        match = {'}':'{', ')': '(', ']': '['}
        stack = []
        for i in s:
            if i not in match:
                stack.append(i)
            elif i in match:
                if len(stack) == 0:
                    return False
                if match[i] != stack.pop():
                    return False
        return True if len(stack) ==0 else False
        