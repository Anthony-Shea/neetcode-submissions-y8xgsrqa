class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = defaultdict(int)
        for c in text:
            if c in "balloon":
                m[c] += 1
        if len(m) == 5:
            m['l'] //=2
            m['o'] //=2
            return min(m.values())
        return 0