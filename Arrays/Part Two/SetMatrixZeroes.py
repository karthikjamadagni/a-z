class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        checkrows = [-1] * n
        checkcols = [-1] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    checkrows[i] = 0
                    checkcols[j] = 0

        for i in range(n):
            for j in range(m):
                if checkrows[i] == 0 or checkcols[j] == 0:
                    matrix[i][j] = 0

        
        