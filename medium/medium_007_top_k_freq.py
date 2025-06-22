# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

# Dada una matriz de palabras de cadena y un entero k, devuelve las k cadenas más frecuentes.

# Devuelve la respuesta ordenada por la frecuencia de mayor a menor. Ordena las palabras con la misma frecuencia por su orden lexicográfico.
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)

        freqs = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        freq_words = list(freqs[i][0] for i in range(len(freqs)))
        return freq_words[:k]


sol = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 3
print(sol.topKFrequent(words, k))

# Runtime: 3ms