class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8 * n)**(1/2)) / 2)