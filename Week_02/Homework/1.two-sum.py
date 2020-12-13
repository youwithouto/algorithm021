class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = dict()
        for i in range(len(nums)):
            current = nums[i]
            theOther = target - current
            if theOther in other:
                return [i, other[theOther]]
            else:
                other[current] = i
