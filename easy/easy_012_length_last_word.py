# 58. Length of Last Words
# https://leetcode.com/problems/length-of-last-word/

# Dada una cadena s que consiste en palabras y espacios, devuelve la longitud de la última palabra en la cadena.

# Una palabra es una subcadena máxima que consiste solo en caracteres que no son espacios.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.lstrip(' ').rstrip(' ').split(' ')[-1])

# Ejemplo:
# Input: s = "Hello World"
# Output: 5

# Runtime: 0ms
