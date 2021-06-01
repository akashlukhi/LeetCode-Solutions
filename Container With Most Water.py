class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxiArea = 0, len(height) - 1, 0
        while(left < right):
            maxiArea = max(maxiArea, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxiArea
