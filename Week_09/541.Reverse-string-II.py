class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sl = list(s)
        left, right = 0, k - 1

        while left < len(sl):
            if right < len(sl):
                # reverse k
                self.doReverseStr(sl, left, right)
                left += 2 * k
                right += 2 * k
            else:
                # reverse till len(s) - 1
                right = len(sl) - 1
                self.doReverseStr(sl, left, right)
                break
        return ''.join(sl)

    def doReverseStr(self, sl: str, left: int, right: int) -> None:
        while left < right:
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -= 1
