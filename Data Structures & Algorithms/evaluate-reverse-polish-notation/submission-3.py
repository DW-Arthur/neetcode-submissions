class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack, push numbers on the stack
        # once you reach an operand, pop the last pushed element
        # Then pop the second last pushed element, use operands between them
        # Push the result to the stack
        # In theory, there should only be 2 numbers max in the stack before we reach an operand
        check = {'+', '-', '*', '/'}
        stack = []
        result = 0
        for i in tokens:
            if i in check:
                y = stack.pop()
                x = stack.pop()
                if i == "+":
                    result = x + y
                if i == "-":
                    result = x - y
                if i == "*":
                    result = x * y
                if i == "/":
                    result = int(x / y)  
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]
            
