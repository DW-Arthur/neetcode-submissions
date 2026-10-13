class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use a stack, get the difference between the indexes
        indices = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                indices[stackInd] = i - stackInd
            stack.append((temperatures[i],i))
        return indices
        
        
        