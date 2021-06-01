class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in [']', ')', '}']:
            return False
        temp = []
        flag = True
        for i in range(len(s)):
            if s[i] in ['[', '(', '{']:
                temp.append(s[i])
            else:
                if len(temp) != 0:
                    check = temp[len(temp) - 1]
                    if s[i] == ')' and check == '(':
                        temp.pop()
                    elif s[i] == ']' and check == '[':
                        temp.pop()
                    elif s[i] == '}' and check == '{':
                        temp.pop()
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break

        if flag and len(temp) == 0 and i == len(s)-1:
            return True
        else:
            return False
