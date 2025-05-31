# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

# Dada una cadena s, compruebe si se puede construir tomando una subcadena de la misma y añadiendo múltiples copias de la subcadena juntas.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length):
            patron = s[:i]
            repeticiones = length // i
            if patron * repeticiones == s:
                return True
        return False
    
# Ejemplo:
# s = "abcabcabcabc"

# Output: True

# Runtime: 103ms

