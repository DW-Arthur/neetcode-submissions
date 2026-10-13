class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Go with 3 x 3 
        row, col = 0,0
        while row <9:
            while col < 9:
                duplicate = set()
                for i in range(row, row+3):
                    for j in range(col, col +3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in duplicate:
                            return False
                        duplicate.add(board[i][j])
                col +=3
            col = 0
            row +=3
        # Check the row
        for i in range(0, 9):
            duplicate = set()
            for j in range(0,9):
                if board[i][j] != "." and board[i][j] in duplicate: 
                    return False
                duplicate.add(board[i][j])
        # Check the col
        for j in range(0, 9):
            duplicate = set()
            for i in range(0,9):
                if board[i][j] != "." and board[i][j] in duplicate: 
                    return False
                duplicate.add(board[i][j])
        return True
        
            
        