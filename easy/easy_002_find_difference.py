# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

# Se te dan dos strings s y t.

# La cadena t se genera mediante la mezcla aleatoria de cadenas s y luego se agrega una letra más en una posición aleatoria.

# Devuelve la letra que se agregó a t.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letra in t:
            if s.count(letra) != t.count(letra):
                return letra

# Ejemplo
# Input: s = "abcd", t = "abcde"
# Output: "e"

# Runtime: 1ms