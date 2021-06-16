class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-1-i):

                temp1 = matrix[i][j]
                temp2 = matrix[j][len(matrix)-i - 1]
                temp3 = matrix[len(matrix)-i-1][len(matrix)-j-1]
                temp4 = matrix[len(matrix)-j-1][i]

                matrix[i][j] = temp4
                matrix[j][len(matrix)-i - 1] = temp1
                matrix[len(matrix)-i-1][len(matrix)-j-1] = temp2
                matrix[len(matrix)-j-1][i] = temp3
