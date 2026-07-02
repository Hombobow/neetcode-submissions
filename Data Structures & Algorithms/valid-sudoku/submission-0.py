class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = [0] * 9
        for r in board:
            for c in r:
                if c == ".":
                    continue
                if checker[int(c) - 1] == 1:
                    return False
                checker[int(c) - 1] += 1
            checker = [0] * 9
        
        for c in range(0, 9):
            for r in range(0, 9):
                if board[r][c] == ".":
                    continue
                entry = int(board[r][c]) - 1
                if checker[entry] == 1:
                    return False
                checker[entry] += 1
            checker = [0] * 9
        
        for r in range(0, 7, 3):
            for c in range(0, 7, 3):
                for r1 in range (r, r + 3):
                    for c1 in range(c, c+3):
                        if board[r1][c1] == ".":
                            continue
                        entry = int(board[r1][c1]) - 1
                        if checker[entry] == 1:
                            return False
                        checker[entry] += 1
                checker = [0] * 9
        
        return True
