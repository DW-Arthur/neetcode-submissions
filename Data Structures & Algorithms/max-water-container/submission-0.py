class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1
        result = 0
        while l < r:
            # Get the area, compare it with the result
            result = max(result,min(heights[l], heights[r]) * (r-l))
            # Move the pointer of the lower one
            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return result
        