# 704. Binary Search
# https://leetcode.com/problems/binary-search/

# Dada una matriz de números enteros que se ordenan en orden ascendente, y un objetivo entero, escriba una función para buscar el objetivo en números. Si el objetivo existe, entonces devuelve su índice. De lo contrario, devuelve -1.

# Debe escribir un algoritmo con complejidad de tiempo de ejecución O(log n).

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        inicio = 0
        fin = len(nums) - 1

        while inicio <= fin:
            medio = (fin + inicio) // 2
            if nums[medio] == target:
                return medio
            elif target > nums[medio]:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1
            
nums = [-1,0,3,5,9,12]
target = 9
        
# Runtime: 0ms