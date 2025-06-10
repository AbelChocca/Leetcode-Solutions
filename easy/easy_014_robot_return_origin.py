# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/

# Hay un robot que comienza en la posición (0, 0), el origen, en un plano 2D. Dada una secuencia de sus movimientos, juzga si este robot termina en (0, 0) después de completar sus movimientos.

# Se le da un movimiento de cadena que representa la secuencia de movimientos del robot donde los movimientos[i] representan su enésim movimiento. Los movimientos válidos son 'R' (derecha), 'L' (izquierda), 'U' (arriba) y 'D' (abajo).

# Devuelve verdadero si el robot regresa al origen después de terminar todos sus movimientos, o falso de lo contrario.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movements = [mov for mov in moves]
        init_position = (0, 0)
        key_mov = {
            'R': lambda x, y: (x + 1, y),
            'L': lambda x, y: (x - 1, y),
            'U': lambda x, y: (x, y + 1),
            'D': lambda x, y: (x, y - 1)
        }
        for mov in movements:
            if mov in key_mov:
                init_position = key_mov[mov](*init_position)
        return init_position == (0, 0)


# Input: moves = "UD"
# Output: true

# Runtime: 35ms