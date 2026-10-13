class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Brute force, 3 passes
        # First pass - go through the rows, check for duplicates
        # Second pass - go through the columns, check for duplicates
        # Third pass - go through the board, 3x3 grid, check for duplicates
        valid = True
        # board[0][0], board[0][1], these are single entries

        for r in range(9):
            seen = set()  # Reset for each row!
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        # Flip r and c to fix the columns and scan for each row
        for c in range(9):
            seen = set()  # Reset for each column!
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for box_r in range(3):
            for box_c in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        val = board[box_r * 3 + r][box_c * 3 + c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True