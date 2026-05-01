class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        I, J = 0, 0
        for i in range(m):
            if matrix[i][0] == 0:
                I = 1
        for j in range(n):
            if matrix[0][j] == 0:
                J = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if I:
            for i in range(m):
                matrix[i][0] = 0
        if J:
            for j in range(n):
                matrix[0][j] = 0


