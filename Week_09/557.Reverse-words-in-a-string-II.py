class Solution:
    def reverseWords(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s
        l = list(s)
        left, right = -1, -1
        for i in range(len(l)):
            c = l[i]
            if c != " " and left == -1:
                left = i
            elif c != " " and left != -1 and right == -1:
                continue
            elif c == " " and left != -1 and right == -1:
                right = i - 1
                self.doReverseStr(l, left, right)
                left, right = -1, -1
            else:
                continue
        if left != -1 and right == -1:
            right = len(l) - 1
            self.doReverseStr(l, left, right)
        return "".join(l)

    def doReverseStr(self, sl: List, left: int, right: int) -> None:
        while left < right:
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -= 1
