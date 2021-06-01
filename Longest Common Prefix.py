class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        ans = strs[0]
        while True:
            l = len(ans)
            flag = True
            for i in range(1, len(strs)):
                if ans not in strs[i][:l]:
                    ans = ans[:l - 1]
                    flag = False
                    break
            if flag:
                return ans
