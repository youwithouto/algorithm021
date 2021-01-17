class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        prev, next = 1, 2
        result = 0
        for i in range(3, n + 1):
            result = prev + next
            prev, next = next, result
        return result
