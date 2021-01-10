class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = nums + [1]
        N = len(nums)
        mem = [[0]*N for i in range(N)]

        for d in range(2, N+1):
            for s in range(-1, N-1):
                f = s + d
                if f >= N:
                    continue
                mem[s][f] = max([mem[s][i] + nums[s] * nums[i]
                                 * nums[f] + mem[i][f] for i in range(s+1, f)])

        return mem[-1][-1]
