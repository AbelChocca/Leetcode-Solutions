# 1502. Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# Una secuencia de números se llama progresión aritmética si la diferencia entre dos elementos consecutivos cualesquiera es la misma.

# Dada una matriz de números arr, devuelve verdadero si la matriz se puede reorganizar para formar una progresión aritmética. De lo contrario, devuelve falso.

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        if len(arr) <= 2:
            return True
        ordered_list = sorted(arr)

        diferences = ordered_list[1] - ordered_list[0]

        for i in range(2, len(arr)):
            if ordered_list[i] - ordered_list[i - 1] != diferences:
                return False
            
        return True

#Ejemplo:
#Input: arr = [1,2,4]
#Output: false

# Runtime: 0ms
