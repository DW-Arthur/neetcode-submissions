class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First determine the row the target is in
        # Once the row is determined, then we will find the target 
        left, right =0, len(matrix[0])-1
        up, down = 0, len(matrix)-1
        while up <= down:
            mid = (up + down)//2
            current = matrix[mid][0]
            if current < target:
                up = mid +1
            elif current > target:
                down -=1
            else:
                return True
        # Once the loop finishes, up and down are equal, search through the row
        while left <= right:
            mid = (left + right)//2
            current = matrix[up][mid]
            if current < target:
                left = mid +1
            elif current > target:
                right = mid -1
            else:
                return True
        return False
        