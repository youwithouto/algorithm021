class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        distance_to_end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= distance_to_end:
                distance_to_end = i
        return distance_to_end == 0
