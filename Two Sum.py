class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in nums:
                ans.append(i)
                ans.append(nums.index(target - nums[i]))
                if ans[0] == ans[1]:
                    ans.clear()
                else:
                    return ans
