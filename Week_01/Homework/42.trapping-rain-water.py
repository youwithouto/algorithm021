class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left, right, totalArea = 0, len(height) - 1, 0
        leftMaxHeight, rightMaxHeight = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMaxHeight = max(leftMaxHeight, height[left])
                totalArea += leftMaxHeight - height[left]
            else:
                right -= 1
                rightMaxHeight = max(rightMaxHeight, height[right])
                totalArea += rightMaxHeight - height[right]
        return totalArea
