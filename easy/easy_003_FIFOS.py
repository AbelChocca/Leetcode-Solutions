# 28. Find the index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

# Ejemplo:   
# haystack = "hello"
# needle = "ll"
# Output: 2

# Runtime: 0ms