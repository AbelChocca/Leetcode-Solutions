# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/

# Dada una matriz de números enteros, ordene la matriz en orden ascendente y devuélvala.

# Debe resolver el problema sin usar ninguna función incorporada en la complejidad de tiempo O(nlog(n)) y con la menor complejidad de espacio posible.

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums: list[int], low: int, high: int):
        if low < high:
            p =  self.partition(nums, low, high)
            self.quick_sort(nums, low, p - 1)
            self.quick_sort(nums, p + 1, high)

    def partition(self, nums, low, high):
        pivote = nums[high] 
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivote:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
#         i
nums = [5,1,1,2,0,0]

sol = Solution()

print(sol.sortArray(nums))
print(nums)

