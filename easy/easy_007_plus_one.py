# 66. Plus One
# https://leetcode.com/problems/plus-one/

# Se le da un número entero grande representado como una matriz entera de dígitos, donde cada dígito[i] es el ésimo del número entero. Los dígitos están ordenados de más significativos a menos significativos en orden de izquierda a derecha. El número entero grande no contiene ningún 0 inicial.

#Aumente el número entero grande en uno y devuelva la matriz de dígitos resultante.
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result_sum = str(int(''.join(f'{digit}' for digit in digits)) + 1)
        result_array = [int(digit) for digit in result_sum]

        return result_array
            

# Ejemplo:
# digits = [4,3,2,1]
# Output: [4,3,2,2]


# Runtime: 0ms 