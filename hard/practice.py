class Solution:
    def sum_of_digits(self, integer: int) -> int:
        numbers = str(integer)
        return sum(int(x) for x in numbers)

    def palindrome(self, integer: int) -> int:
        number_reverse = reversed(str(integer))
        result =  int(''.join(number_reverse))
        return result == integer

    def armstrong(self, integer: int) -> int:
        string = str(integer)
        numbers = [pow(int(x), len(string)) for x in string]
        return sum(numbers) == integer
    
    def invert_num(self, integer: int) -> int:
        string = reversed(str(integer))
        return int(''.join(string))
    
    def decimal_to_binary(self, integer: int) -> int:
        digits = []
        while integer > 0:
            digits.append(integer % 2)
            integer = integer // 2

        binary = reversed(digits)
        result = int(''.join(map(lambda x: str(x), binary)))
        return result
    # geometry
    def poligon_area(self, arr: list[int]) -> int:
        x1, y1 = arr[0]
        x2, y2 = arr[1]
        x3, y3 = arr[2]

        return 0.5 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    def distance(self, arr: list[int]) -> int:
        x1, y1 = arr[0]
        x2, y2 = arr[1]

        return (pow(x2 - x1, 2) + pow(y2 - y1, 2)) ** 0.5

sol = Solution()


integer = 13
points = [[0, 0], [4, 0], [0, 3]]
two_points = [[4, 5], [5, 7]]

print(sol.decimal_to_binary(integer))
print(sol.poligon_area(points))
print(sol.distance(two_points))