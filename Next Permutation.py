class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        while (i >= 0 and nums[i+1] <= nums[i]):
            i -= 1
        if (i >= 0):
            j = len(nums) - 1
            while(nums[j] <= nums[i]):
                j -= 1
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
        k = i + 1
        l = len(nums)-1
        while(k < l):
            temp = nums[k]
            nums[k] = nums[l]
            nums[l] = temp
            k += 1
            l -= 1
