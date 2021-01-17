class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(left: int, right: int, current: str):
            if left == 0 and right == 0:
                result.append(current)
                return
            if left > 0:
                helper(left - 1, right + 1, current + "(")
            if right > 0:
                helper(left, right - 1, current + ")")
        helper(n, 0, "")

        return result
