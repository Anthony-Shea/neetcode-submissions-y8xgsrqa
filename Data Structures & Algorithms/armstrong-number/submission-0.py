class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = 0
        m = n
        r = 0
        while m > 1:
            m /= 10
            k += 1
        a = list(str(n))
        for num in a:
            r += int(num)**k
        return r == n