# 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# Se le da una matriz de coordenadas, coordenadas[i] = [x, y], donde [x, y] representa la coordenada de un punto. Compruebe si estos puntos forman una línea recta en el plano XY.



class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]

            if (y1 - y0)*(x - x1) != (y - y1) * (x1 - x0):
                return False
        return True
    

sol = Solution()
coordinates = [[0,0],[0,1],[0,-1]]
print(sol.checkStraightLine(coordinates))

# Runtime: 0ms