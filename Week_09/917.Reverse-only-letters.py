class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if S is None or len(S) == 0:
            return S
        l = list(S)
        al, index2C = [], {}
        for i in range(len(l)):
            c = l[i]
            if c.isalpha():
                al.append(c)
            else:
                index2C[i] = c
        self.doReverseStr(al, 0, len(al) - 1)
        result = []
        j = 0
        for i in range(len(S)):
            if i in index2C:
                result.append(index2C[i])
            elif j < len(al):
                result.append(al[j])
                j += 1
        if j < len(al):
            result += al[j:]
        return "".join(result)

    def doReverseStr(self, sl: List, left: int, right: int) -> None:
        while left < right:
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -= 1
