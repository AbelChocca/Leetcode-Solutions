# 1822. Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

#Implemente una función signFunc(x) que devuelve:
# 1 si x es positivo.
# -1 si x es negativo.
# 0 si x es igual a 0.
# Se le da una matriz de números enteros. Deje que el producto sea el producto de todos los valores en los números de la matriz.
# Devolver signFunc (producto).

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product_number = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                product_number *= -1
        return product_number

# Ejemplo:
# nums = [-1,-2,-3,-4,3,2,1]
# Output: 1

# Runtime: 0ms