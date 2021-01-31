class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        dp = [0] * l
        result = 0
        for i in range(l):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > result:
                    result = dp[i]
        return result
