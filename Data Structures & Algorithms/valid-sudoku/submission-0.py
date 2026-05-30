class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(9):
            counter = dict()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in counter.keys():
                        return False
                    else:
                        counter[board[i][j]] = None
                    
        for j in range(9):
            counter = dict()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in counter.keys():
                        return False
                    else:
                        counter[board[i][j]] = None

        for (a,b) in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            counter = dict()
            for i in range(a, a+3):
                for j in range(b, b+3):
                    if board[i][j] != '.':
                        if board[i][j] in counter.keys():
                            return False
                        else:
                            counter[board[i][j]] = None


        return True