# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/

# Se le da una lista de operaciones de cadenas, donde operations[i] es la enésima operación que debe aplicar al registro y es una de las siguientes:

# Un entero x.

# Registra una nueva puntuación de x.

# '+'

# Registre una nueva puntuación que sea la suma de las dos puntuaciones anteriores.

# 'D'

# Registre una nueva puntuación que sea el doble de la puntuación anterior.

# 'C'

# Invalidar la puntuación anterior, eliminándola del registro.

# Devuelve la suma de todas las puntuaciones del registro después de aplicar todas las operaciones.

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for operator in operations:
            if operator == '+':
                scores.append(scores[-1] + scores[-2])
            elif operator == 'D':
                scores.append(scores[-1]*2)
            elif operator == 'C': 
                scores.pop()
            else:
                scores.append(int(operator))
        return sum(scores)
            

# Ejemplo
# Input: ops = ["5","2","C","D","+"]
# Output: 30

# Runtime: 0ms