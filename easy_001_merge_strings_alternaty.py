# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

# Dado dos strings word1 y word2, combinar alternando caracteres de ambos.
# Si uno es más largo, añade el resto al final

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        output_string = ''.join(f'{word1[i]}{word2[i]}' for i in range(min(length1, length2)))
        if length1 > length2:
            output_string += f'{word1[length2:]}'
            return output_string
        output_string += f'{word2[length1:]}'
        return output_string

# Ejemplo:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"       
# Runtime: 37ms
