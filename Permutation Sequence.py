class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1,n+1)]
        ans = list(itertools.permutations(arr))
        s = "".join(str(ans[k-1]))
        s = s.replace("(","")
        s = s.replace(")","")
        s = s.replace(",","")
        s = s.replace(" ","")
        return s