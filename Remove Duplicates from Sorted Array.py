class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return len(nums)
