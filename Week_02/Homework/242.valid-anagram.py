class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        for c in t:
            if c in map:
                map[c] -= 1
            else:
                return False
        for _, v in map.items():
            if v > 0:
                return False
        return True
