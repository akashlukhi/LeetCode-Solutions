class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, length, st, e = 0, 0, 0, 0
        if len(s) == 1:
            return s
        for j in range(len(s)):
            start = j
            for i in range(j + 1, len(s)):
                if s[start] == s[i]:
                    temp = s[start:i + 1]
                    temp2 = temp[::-1]
                    if temp == temp2 and length < i - start:
                        st = start
                        e = i + 1
                        length = i - start
        if st-e == 0:
            return s[0]
        else:
            return s[st:e]
