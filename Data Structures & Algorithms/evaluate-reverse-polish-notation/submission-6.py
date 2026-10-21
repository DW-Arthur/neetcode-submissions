class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                right = array.pop()
                left = array.pop()
                array.append(left+right)
            elif tokens[i] == "-":
                right = array.pop()
                left = array.pop()
                array.append(left-right)
            elif tokens[i] == "*":
                right = array.pop()
                left = array.pop()
                array.append(left*right)
            elif tokens[i] == "/":
                right = array.pop()
                left = array.pop()
                array.append(int(left/right))
            else:
                array.append(int(tokens[i]))
        return array.pop()

