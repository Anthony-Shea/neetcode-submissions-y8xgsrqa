class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            n &= (n - 1)
            r += 1
        return r