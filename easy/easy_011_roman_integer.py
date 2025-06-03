# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Por ejemplo, 2 se escribe como II en número romano, solo dos se suman. 12 se escribe como XII, que es simplemente X + II. El número 27 se escribe como XXVII, que es XX + V + II.

#Los números romanos generalmente se escriben de mayor a menor de izquierda a derecha. Sin embargo, el número de cuatro no es IIII. En cambio, el número cuatro se escribe como IV. Debido a que el uno está antes de los cinco, lo restamos haciendo cuatro. El mismo principio se aplica al número nueve, que se escribe como IX. Hay seis casos en los que se utiliza la resta:

#Me pueden colocar antes de V (5) y X (10) para hacer 4 y 9.

#X se puede colocar antes de L (50) y C (100) para hacer 40 y 90.

#C se puede colocar antes de D (500) y M (1000) para hacer 400 y 900.

#Dado un número romano, conviértalo en un número entero.

class Solution:
    def romanToInt(self, s: str) -> int:
        output_integer = 0
        i = 0
        symbols = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        while i < len(s):
            if i + 1 < len(s) and s[i] + s[i+1] in symbols:
                output_integer += symbols[s[i] + s[i+1]]
                i += 2
            else:
                output_integer += symbols[s[i]]
                i += 1
                
        return output_integer

# Ejemplo
# Input: nums = "MCMXCIV"
# Output: 1994

# Runtime: 12ms
