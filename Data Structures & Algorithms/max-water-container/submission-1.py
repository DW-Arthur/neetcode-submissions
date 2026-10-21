class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force - Nested for loop to calculate the container of every possible area
        # Optimal - 2 pointer
        # left and right, starting from beginning and end
        # When start from beginning to end, the length is the highest, only the height
        # matters now
        # Have a max counter
        max_total = -1
        left,right = 0, len(heights)-1
        # Always move the shorter side
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            max_total = max(max_total,area)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right -=1
        return max_total


        