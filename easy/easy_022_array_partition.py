# 561. Array Partition
# https://leetcode.com/problems/array-partition/

# Dada una matriz entera nums de 2n enteros, agrupe estos enteros en n pares (a1, b1), (a2, b2), ..., (an, bn) de tal manera que se maximice la suma de min(ai, bi) para todos los i. Devuelve la suma maximizada.

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # ordenamos
        nums.sort()

        return sum(nums[i] for i in range(0, len(nums), 2))
        
        

nums = [1,4,3,2]

sol = Solution()

# Runtime: 25ms