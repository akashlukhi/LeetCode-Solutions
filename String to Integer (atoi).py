class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        sign = '+'
        sign_count = 0
        flag = True
        for i in range(len(s)):
            if s[i] == ' ' and flag:
                continue
            elif sign_count == 2:
                break
            elif s[i] == '-' and flag:
                sign = '-'
                flag = False
                sign_count += 1
                continue
            elif s[i] == '+' and flag:
                sign_count += 1
                flag = False
                continue
            elif s[i] >= '0' and s[i] <= '9':
                ans += s[i]
                flag = False
            else:
                break
        if len(ans) == 0:
            return 0
        ans = int(ans)
        if sign == '-':
            ans = -abs(ans)
        if ans >= 2147483647:
            ans = min(ans, 2**31 - 1)
        elif ans <= -2147483648:
            ans = max(ans, -(2**31))
        return ans
