class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use a stack, get the difference between the indexes
        indices = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    prevIndex = stack.pop()
                    indices[prevIndex] = i - prevIndex
            stack.append(i)
        return indices
        
        
        