from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 1: Find the target row
        top, bot = 0, ROWS - 1
        target_row = -1

        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                target_row = mid
                break

        # Target is outside the range of the whole matrix
        if target_row == -1:
            return False

        # Step 2: Binary search inside the selected row
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            current = matrix[target_row][mid]
            if current < target:
                left = mid + 1
            elif current > target:
                right = mid - 1
            else:
                return True

        return False