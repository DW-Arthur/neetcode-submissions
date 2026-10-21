from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n - 1, -1, -1):
            # 1. Pop all elements that are smaller or equal (they can't be warmer days)
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # 2. If stack still has elements, top of stack is the next warmer day
            if stack:
                result[i] = stack[-1] - i

            # 3. Push current day index onto stack
            stack.append(i)

        return result