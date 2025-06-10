# 1041. Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/

# En un plano infinito, un robot inicialmente se para en (0, 0) y mira hacia el norte. Tenga en cuenta que:

# La dirección norte es la dirección positiva del eje y.

# La dirección sur es la dirección negativa del eje y.

# La dirección este es la dirección positiva del eje x.

# La dirección oeste es la dirección negativa del eje x.

# El robot puede recibir una de tres instrucciones:

# "G": ir recto 1 unidad.

# "L": gire 90 grados a la izquierda (es decir, en sentido contrario a las agujas del reloj).

# "R": gire 90 grados hacia la derecha (es decir, en el sentido de las agujas del reloj).

# El robot realiza las instrucciones dadas en orden y las repite para siempre.

# Devuelve verdadero si y solo si existe un círculo en el plano de tal manera que el robot nunca salga del círculo.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_index = 0
        dir = 'North'
        init_position = (0, 0)
        directions = {
            'North': lambda x, y: (x, y + 1),
            'West': lambda x, y: (x - 1, y),
            'South': lambda x, y: (x, y - 1),
            'East': lambda x, y: (x + 1, y)
        }
        dir_keys = list(directions.keys())
        for instruct in instructions:
            if instruct == 'L':
                dir_index = (dir_index + 1) % 4
                dir = dir_keys[dir_index]
            if instruct == 'R':
                dir_index = (dir_index + 3) % 4
                dir = dir_keys[dir_index]
            if instruct == 'G':
               init_position = directions[dir](*init_position)
            
        return init_position == (0, 0) or dir_index != 0
            
sol = Solution()
print(sol.isRobotBounded("GLRLLGLL"))
