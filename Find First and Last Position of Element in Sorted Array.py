class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            start = nums.index(target)
            nums.sort(reverse=True)
            end = nums.index(target)
            return [start, len(nums) - end - 1]
