class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend <= 0 and divisor < 0) or (dividend >= 0 and divisor > 0):
            ans = abs(dividend)//abs(divisor)
            if ans >= 2147483648:
                return 2147483647
            else:
                return ans
        if (dividend <= 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
            ans = abs(dividend)//abs(divisor)
            if -abs(ans) <= -2147483648:
                return -2147483648
            else:
                return -abs(ans)
