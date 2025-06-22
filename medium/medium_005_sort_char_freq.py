# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

# Dada una cadena s, ordénela en orden decreciente según la frecuencia de los caracteres. La frecuencia de un carácter es el número de veces que aparece en la cadena.

# Devuelve la cadena ordenada. Si hay varias respuestas, devuelve cualquiera de ellas.

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        dec_order = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for key, val in dec_order:
            result += key * val
        return result
        

sol = Solution()

s = "cccaaa"

print(sol.frequencySort(s))

# Runtime: 6ms