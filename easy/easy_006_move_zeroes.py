# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Dada una matriz entera nums, mueva todos los 0 al final de la mientras mantiene el orden relativo de los elementos distintos de cero.

# Tenga en cuenta que debe hacer esto en el lugar sin hacer una copia de la matriz.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        first_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[first_zero], nums[i] = nums[i], nums[first_zero]
                first_zero += 1

# Ejemplo:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Runtime: 2ms