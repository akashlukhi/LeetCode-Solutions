class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        words = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], [
            "m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        temp = []
        ans = []
        if len(digits) == 0:
            return ans
        elif len(digits) == 1:
            return words[int(digits[0])-2]
        else:
            temp = words[int(digits[0])-2]
            for i in range(1, len(digits)):
                if len(ans) > 0:
                    temp = ans.copy()
                    ans.clear()
                for j in range(len(temp)):
                    for k in range(len(words[int(digits[i])-2])):
                        ans.append(temp[j] + words[int(digits[i])-2][k])
            return ans
