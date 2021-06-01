class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        ans = 0
        while(x != 0):
            temp = x % 10
            ans = ans * 10 + temp
            x //= 10
        if ans >= 2147483647 or ans <= -2147483648:
            return 0
        if flag:
            return -abs(ans)
        else:
            return ans
