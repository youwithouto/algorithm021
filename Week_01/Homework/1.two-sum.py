class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            current = nums[i]
            theOther = target - current
            if theOther in numToIndex:
                return [i, numToIndex[theOther]]
            numToIndex[current] = i
