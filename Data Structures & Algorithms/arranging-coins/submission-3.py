class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        res = 0
        num = 0
        while n > 0:
            num = num + 1
            res += 1
            n -= num
        return res - 1