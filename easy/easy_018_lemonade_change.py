# 860. Lemonade Change
# https://leetcode.com/problems/lemonade-change/

# En un puesto de limonada, cada limonada cuesta 5 $. Los clientes están haciendo cola para comprarle y pedir uno a la vez (en el orden especificado por las facturas). Cada cliente solo comprará una limonada y pagará con un billete de 5, 10 $ o 20 $. Debe proporcionar el cambio correcto a cada cliente para que la transacción neta sea que el cliente pague 5 $.

# Tenga en cuenta que al principio no tiene ningún cambio en la mano.

# Dada una matriz entera de facturas donde bills[i] es la factura que paga el i- cliente, devuelve verdadero si puede proporcionar a cada cliente el cambio correcto, o falso de lo contrario.

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


sol = Solution()

bills = [5,5,10,10,20]

print(sol.lemonadeChange(bills))

# Runtime: 4ms