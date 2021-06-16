class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans  = []
        row = len(matrix)
        col = len(matrix[0])
        while matrix:
            ans.extend(matrix[0])
            matrix.pop(0)
           
            if matrix and len(matrix[0])!=0:
                for i in range(len(matrix)):
                    ans.append(matrix[i][len(matrix[i])-1])
                    matrix[i].pop()
               
            if matrix and len(matrix[0])!=0:
                temp = matrix[len(matrix)-1]
                temp.reverse()
                ans.extend(temp)
                matrix.pop()
            if matrix and len(matrix[0])!=0:
                for i in range(len(matrix)-1,-1,-1):
                    ans.append(matrix[i][0])
                    matrix[i].pop(0)
        return ans