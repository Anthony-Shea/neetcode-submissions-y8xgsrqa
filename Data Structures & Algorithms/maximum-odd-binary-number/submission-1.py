class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        r = ""
        if c['1'] != 1:

            for _ in range(c['1'] - 1):
                r += '1'
        for _ in range(c['0']):
            r += '0'
        r += '1'
        return r