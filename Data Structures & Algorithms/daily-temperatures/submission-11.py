class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use stack to store the temperatures, 2 indices, (temperature, index)
        # 30, 38
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()
                result[index] = i -index
            stack.append([i, temperatures[i]])
        return result
