class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(10):
            digits = list(str(n))
            n = 0
            for digit in digits:
                n += int(digit)**2
        if n == 1:
            return True
        else:
            return False