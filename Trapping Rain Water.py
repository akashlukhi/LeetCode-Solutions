class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            if height[:i]:
                left = max(height[:i])
            else:
                left = 0
            if height[i+1:]:
                right = max(height[i+1:])
            else:
                right = 0
            mini = min(left, right)

            if mini != 0 and mini > height[i]:
                ans += abs(mini-height[i])
        return ans
