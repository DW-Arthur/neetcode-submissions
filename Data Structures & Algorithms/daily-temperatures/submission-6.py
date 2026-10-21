class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal Solution, try going from reverse direction
        # Use a stack
        # If stack is empty, set the result to distane 0
        # If the top of the stack is more than the current index, pop it and keep searching
        stack = []
        result = [0] * len(temperatures)
        # Go in reverse
        for i in range(len(temperatures)-1, -1, -1):
            # if stack is not empty, compare values
            # if the top of stack is less, keep popping until its empty or you reached
            # a smaller element
            while stack:
                if temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                    continue
                # Stack is not empty, but reached a bigger element
                diff = stack[-1] - i
                result[i] = diff
                stack.append(i)
                break
            # If all the elements of stack is popped, no bigger element found,
            # Add the new biggest element to the stack 
            if len(stack) == 0:
                stack.append(i)
        return result