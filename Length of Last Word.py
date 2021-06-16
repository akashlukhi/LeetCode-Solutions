class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(s.split(' '))
        while (l and l[len(l)-1] == ""):
            l.pop(len(l)-1) 
        if l:
            return len(l[len(l)-1])
        else:
            return 0