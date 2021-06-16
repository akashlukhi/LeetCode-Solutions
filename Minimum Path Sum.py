class Solution:
    def minPathSum(self, board: List[List[int]]) -> int:
        m,n = len(board), len(board[0])
        maxi = 0
        for i in range(m):
            maxi += sum(board[i])
        print(maxi)
        for i in range(m):
            for j in range(n):  
                if i ==0 and j==0:
                    continue
                board[i][j] += min((board[i-1][j] if i else maxi), (board[i][j-1] if j else maxi))
        print(board)
        return board[m-1][n-1]