class Solution:
    def maxDifference(self, s: str) -> int:
        m = Counter(s)
        r = float("-inf")
        for o in m.values():
            if o % 2 == 0: continue
            for e in m.values():
                if e % 2 == 1: continue
                r = max(r, (o - e))
        return r
