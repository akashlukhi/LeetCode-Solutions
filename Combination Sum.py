class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        unique = {}
        candidates = list(set(candidates))
        self.solve(candidates, target, result, unique)
        return result

    def solve(self, candidates, target, result, unique, current=[]):
        if target < 0:
            return
        if target == 0:
            temp = current.copy()
            temp1 = temp.copy()
            temp.sort()
            temp = tuple(temp)
            if temp not in unique:
                unique[temp] = 1
                result.append(temp1)
            return
        for i in range(len(candidates)):
            current.append(candidates[i])
            self.solve(candidates, target -
                       candidates[i], result, unique, current)
            current.pop()
