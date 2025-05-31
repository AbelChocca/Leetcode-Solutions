# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# Dadas dos cadenas s y t, devuelve verdadero si t es un anagrama de s, y falso de lo contrario.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# Ejemplo:
# s = "anagram"
# t = "nagaram"

# Output = True

# Runtime: 18ms