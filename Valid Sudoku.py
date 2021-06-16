class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = []
        for i in range(9):
            l.clear()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in l:
                    return False
                l.append(board[i][j])
                
        for i in range(9):
            l.clear()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in l:
                    return False
                l.append(board[j][i])
        
        i,j = 0, 0
        for m in range(0,9,3):
            for n in range(0,9,3):
                l.clear()
                for i in range(3):
                    for j in range(3):
                        if board[m+i][n+j] != "." and board[m+i][n+j] in l:
                            print('ff')
                            return False
                        l.append(board[m+i][n+j])
        
        return True