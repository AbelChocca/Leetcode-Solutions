# 1672. Richest Customer Wealth
# Se le da una cuenta de cuadrícula entera m x n donde las cuentas[i][j] son la cantidad de dinero que el cliente tiene en el banco j. Devuelve la riqueza que tiene el cliente más rico.

# La riqueza de un cliente es la cantidad de dinero que tiene en todas sus cuentas bancarias. El cliente más rico es el cliente que tiene la máxima riqueza.

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for wealth in accounts:
            customer_weatlh = sum(wealth)
            max_wealth = customer_weatlh if customer_weatlh > max_wealth else max_wealth
        return max_wealth
    
sol = Solution()

print(sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))