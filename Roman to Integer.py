class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        word = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = [1, 5, 10, 50, 100, 500, 1000]
        i = 0
        while i < len(s)-1:
            if word.index(s[i]) < word.index(s[i+1]):
                if s[i] == 'I':
                    if s[i+1] == 'V':
                        ans += 4
                    else:
                        ans += 9
                elif s[i] == 'X':
                    if s[i+1] == 'L':
                        ans += 40
                    else:
                        ans += 90
                else:
                    if s[i+1] == 'D':
                        ans += 400
                    else:
                        ans += 900
                i += 1
            else:
                ans += num[word.index(s[i])]
            i += 1
        if i < len(s):
            ans += num[word.index(s[i])]
        return ans
