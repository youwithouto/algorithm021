class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()

        g_length, s_length = len(g), len(s)
        i, j = 0, 0

        while i < g_length and j < s_length:
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result
