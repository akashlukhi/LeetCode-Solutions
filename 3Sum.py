class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if (i != 0 and nums[i] == nums[i - 1]):
                continue
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                if (nums[i] + nums[j] + nums[k] == 0):
                    temp = list([nums[i], nums[j], nums[k]])
                    ans.append(temp)
                    j += 1
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
                elif (nums[i] + nums[j] + nums[k] < 0):
                    j += 1
                else:
                    k -= 1
        return ans
