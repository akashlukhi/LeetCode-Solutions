class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        ans = ''
        cycle = 2 * numRows - 2
        for i in range(0, numRows):
            for j in range(0, len(s) - i, cycle):
                ans += s[j + i]
                if (i != 0 and i != numRows - 1 and j + cycle - i < len(s)):
                    ans += s[j + cycle - i]

        return ans
