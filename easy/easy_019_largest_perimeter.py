# 976. Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/

# Dado un número de matriz entero, devuelve el perímetro más grande de un triángulo con un área distinta de cero, formado a partir de tres de estas longitudes. Si es imposible formar cualquier triángulo de un área distinta de cero, devuelva 0.

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if b + c > a:
                return a + b + c
        return 0

sol = Solution()

nums = [3,6,2,3]
print(sol.largestPerimeter(nums))
# Output: 5