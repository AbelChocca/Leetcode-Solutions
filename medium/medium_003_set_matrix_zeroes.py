# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

# Dada una matriz entera m x n, si un elemento es 0, establezca toda su fila y columna en 0.

# Debes hacerlo en el lugar.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for k in range(rows*cols):
            i = k // cols
            j = k % cols

            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
        for row in zero_rows:
            matrix[row] = [0] * cols

        for row in range(rows):
            for col in zero_cols:
                matrix[row][col] = 0

# Ejemplo:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Runtime: 3ms