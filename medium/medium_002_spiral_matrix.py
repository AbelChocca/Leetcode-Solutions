# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# Dada una matriz m x n, devuelve todos los elementos de la matriz en orden espiral.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral_order = []

        if not matrix:
            return spiral_order

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                spiral_order.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                print(row)
                spiral_order.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral_order.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral_order.append(matrix[row][left])
                left += 1

        return spiral_order
    
sol = Solution()

print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
                