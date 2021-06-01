class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = sys.maxsize
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                s = nums[i] + nums[j] + nums[k]
                if (abs(target - s) < abs(target - ans)):
                    ans = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return ans
