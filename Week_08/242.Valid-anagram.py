class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se = set(s)
        if se == set(t):
            for i in se:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False
