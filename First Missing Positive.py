class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if i == 1:
                ans = 1
                break
        if ans == 0:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        for i in range(len(nums)):
            nums[(nums[i] - 1) % len(nums)] += len(nums)

        for i in range(len(nums)):
            if nums[i] <= len(nums):
                return(i + 1)
        return(len(nums) + 1)
