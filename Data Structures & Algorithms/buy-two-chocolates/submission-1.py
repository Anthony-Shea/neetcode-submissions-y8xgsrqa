class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m1 = m2 =  float('inf')
        for p in prices:
            if p < m1:
                m1, m2 = p, m1
            elif p < m2:
                m2 = p
        leftover = money - m1 - m2
        return leftover if leftover >= 0 else money
            