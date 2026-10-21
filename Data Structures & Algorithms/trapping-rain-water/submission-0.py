class Solution:
    def trap(self, height: List[int]) -> int:
        # Optimal
        # Have 2 arrays in this case
        # Left array[i] contains the highest box to the left of the array 
        # Right array[i] contains the higest box to the right of the array
        # The contained water at i is min(left[i], right[i]) * height[i]
        # Make sure to include the current index in the left and right calculations
        result = 0
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[len(height)-1]= height[len(height)-1]
        for i in range(1,len(height)):
            left[i] = max(left[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        # The current height formula should be min(left[i], right[i]) - height[i]
        for i in range(len(height)):
            result += min(left[i], right[i]) - height[i]
        return result
