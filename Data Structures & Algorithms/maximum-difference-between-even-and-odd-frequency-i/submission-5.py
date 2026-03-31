class Solution:
    def maxDifference(self, s: str) -> int:
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        biggestOdd, smallestEven = -9999, 9999
        for c in m:
            if m[c] % 2 == 0 and m[c] < smallestEven:
                smallestEven = m[c]
            if m[c] % 2 != 0 and m[c] > biggestOdd:
                biggestOdd = m[c]
        return biggestOdd - smallestEven
