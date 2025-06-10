# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        win_conditions = [
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]]
        ]
        for i in range(len(moves)):
            turn = 'X' if i % 2 == 0 else 'O'
            row, col = moves[i][0], moves[i][1]
            grid[row][col] = turn
        
        for condition in win_conditions:
            player_one_condition = all(grid[y][x] == 'X' for y, x in condition)
            player_two_condition = all(grid[y][x] == 'O' for y, x in condition)

            if player_one_condition:
                return "A"
            elif player_two_condition:
                return "B"
                
        if all(not '' in file for file in grid):
            return "Draw"
        return "Pending"

sol = Solution()

print(sol.tictactoe([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]))