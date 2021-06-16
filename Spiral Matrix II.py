class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans  = [[0 for j in range(n)] for i in range(n)]
        row,col = n,n
        temp = 1
        i = 0
        j = 0
        temprow, tempcol = row, col
        startrow, startcol = -1, -1
        while temp <= n*n:
            while temp <= n*n and j != tempcol:
                ans[i][j] = temp
                j+= 1
                temp += 1
            i += 1
            j -= 1
            while temp <= n*n and i != temprow:
                ans[i][j]=temp
                temp += 1
                i += 1
            j -= 1
            i -= 1
            while temp <= n*n and j != startcol:
                ans[i][j]= temp
                temp += 1
                j -= 1
            i -= 1
            j += 1
            while temp <= n*n and i != startrow+1:
                ans[i][j]= temp
                temp += 1
                i -= 1
            startrow += 1
            startcol += 1
            temprow -= 1
            tempcol -=1
            i, j = startrow + 1, startcol +1
        return ans