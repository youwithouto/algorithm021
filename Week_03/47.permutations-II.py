class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            new_result = []
            for r in result:
                for i in range(len(r) + 1):
                    new_result.append(r[:i] + [n] + r[i:])
                    if i < len(r) and r[i] == n:
                        break
            result = new_result
        return result
