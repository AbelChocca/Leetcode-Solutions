# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# Se le dan dos matrices enteras nums1 y nums2, ordenadas en orden no decreciente, y dos enteros m y n, que representan el número de elementos en nums1 y nums2 respectivamente.

# Fusionar nums1 y nums2 en una sola matriz ordenada en orden no decreciente.

# La matriz ordenada final no debe ser devuelta por la función, sino almacenada dentro de la matriz nums1. Para acomodar esto, nums1 tiene una longitud de m + n, donde los primeros m elementos denotan los elementos que deben fusionarse, y los últimos n elementos se establecen en 0 y deben ignorarse. nums2 tiene una longitud de n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        result += nums1[i:m]
        result += nums2[j:n]
        
        for k in range(m+n):
            nums1[k] = result[k]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()

sol.merge(nums1, m, nums2, n)
print(nums1)