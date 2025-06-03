# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/

# Una matriz es monótona si aumenta o disminuye monótonamente.

# Una matriz nums es un aumento monótono si para todos i <= j, nums[i] <= nums[j]. Una matriz de números es monótona disminuyendo si para todos i <= j, nums[i] >= nums[j].

# Dado un número de matriz entero, devuelve verdadero si la matriz dada es monótona, o falso de lo contrario.

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(nums[i] <= nums[i + 1] for i in range(len(nums)-1)) or all(nums[i] >= nums[i + 1] for i in range(len(nums)-1))



# Ejemplo
# Input: nums = [1,2,2,3]
# Output: true

# Runtime: 35ms