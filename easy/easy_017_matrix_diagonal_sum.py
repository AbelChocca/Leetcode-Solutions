# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/

#Dada una estera de matriz cuadrada, devuelve la suma de las diagonales de la matriz.

#Solo incluya la suma de todos los elementos en la diagonal primaria y todos los elementos en la diagonal secundaria que no forman parte de la diagonal primaria.

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:

        return sum(list(mat[i][j] for j in range(len(mat)) 
                        for i in range(len(mat)) 
                        if i == j or j == len(mat) - 1 - i))
    
mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
sol = Solution()
print(sol.diagonalSum(mat))