class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n1, n2 = 0, 0
        for digit in num1:
            n1 = 10 * n1 + value[digit]
        for digit in num2:
            n2 = 10 * n2 + value[digit]
        mul = n1 * n2
        ans = ''
        if mul == 0:
            return "0"
        while mul > 0:
            temp = mul % 10
            mul //= 10
            for key, val in value.items():
                if val == temp:
                    ans = key + ans
                    break
        return ans
