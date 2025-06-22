# 3085. Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

# Se le da una palabra de cadena y un entero k.

# Consideramos que la palabra es k-especial si |freq(word[i]) - freq(word[j])| <= k para todos los índices i y j en la cadena.

# Aquí, freq(x) denota la frecuencia del carácter x en word, y |y| denota el valor absoluto de y.

# Devuelve el número mínimo de caracteres que necesitas eliminar para que la palabra k sea especial.

from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        freqs = list(count.values())
        freqs.sort()

        mininum_deleted = float('inf')
        
        for i in range(len(freqs)):
            target = freqs[i]
            deleted = 0

            for freq in freqs:
                if freq < target:
                    deleted += freq
                elif freq > target + k:
                    deleted += freq - (target + k)
            
            mininum_deleted = min(mininum_deleted, deleted)
        return mininum_deleted


sol = Solution()
word = "dabdcbdcdcd"
k = 2
print(sol.minimumDeletions(word, k))

# Runtime: 57 ms