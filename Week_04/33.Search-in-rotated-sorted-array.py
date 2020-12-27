class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[0] <= nums[mid] and (target > nums[mid] or target < nums[0]):
                low = mid + 1
            elif target > nums[mid] and target < nums[0]:
                low = mid + 1
            else:
                high = mid
        return low if low == high and nums[low] == target else -1
