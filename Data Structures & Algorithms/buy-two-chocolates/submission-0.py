class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if len(prices) >= 2:
            a = prices[0] + prices[1]
        if a <= money:
            return money-a
        else:
            return money