# hashmap
from collections import Counter


class Solution:
    def count_letters(self, string: str) -> dict:
        letters = string.split(" ")
        count = {}

        for letter in letters:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1 
        return count
    
    def count_letter(self, string: str) -> dict:
        return Counter(string.replace(" ", ""))

frase = "hola que tal como estas"

sol = Solution()

print(sol.count_letter(frase))