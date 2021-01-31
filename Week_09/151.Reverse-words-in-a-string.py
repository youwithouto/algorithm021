class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split()
        l.reverse()
        return " ".join(l)
