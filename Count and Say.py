class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        while n-1 :
            temp = ans[0]
            count = 0
            tempans = ""
            for i in range(len(ans)) :
                if ans[i] == temp :
                    count += 1
                else :
                    tempans += str(count)+str(temp)
                    temp = ans[i]
                    count = 1                
            tempans += str(count)+str(temp)
            ans = tempans
            n -= 1
        return ans