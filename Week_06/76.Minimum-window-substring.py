class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCount = len(t)
        i, result = 0, (0, float('inf'))

        for j, c in enumerate(s):
            if need[c] > 0:
                needCount -= 1
            need[c] -= 1
            if needCount == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < result[1] - result[0]:
                    result = (i, j)
                need[s[i]] += 1
                needCount += 1
                i += 1
        return '' if result[1] > len(s) else s[result[0]:result[1] + 1]
