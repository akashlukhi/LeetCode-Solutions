class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        t = []
        l = []
        c = strs.count("")
        for i in range(c):
            t.append("")
            strs.remove("")
        if t:
            ans.append(list(t))
        while strs:
            temp = strs.pop(0)
            t.clear()
            t.append(temp)
            l.clear()
            l[:0] = temp
            for i in strs:
                flag = True
                if len(l) == len(i):
                    for j in range(len(l)):
                        if l[j] not in i or l[j] =='' or l.count(l[j])!= i.count(l[j]):
                            flag = False
                            break
                    if flag:
                        t.append(i)
            for i in t:
                if i in strs:
                    strs.remove(i)
            ans.append(list(t))
        return ans