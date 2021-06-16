class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                if i == 0:
                    return 0
                else:
                    return i
        return len(nums)