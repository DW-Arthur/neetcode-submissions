class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # To use a stack, the stack store pairs, (temperature, index)
        result = [0] * len(temperatures)
        # 30 38 30 36 35 40 28
        # 0  1  2   3  4  5  6 
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                tmp, index = stack.pop()
                result[index] = i - index
            stack.append((temperatures[i], i))
        return result
