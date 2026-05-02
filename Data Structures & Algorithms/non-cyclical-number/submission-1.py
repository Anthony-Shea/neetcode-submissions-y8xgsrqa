class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(9):
            digits = list(str(n))
            n = 0
            for digit in digits:
                n += int(digit)**2
        return n == 1
