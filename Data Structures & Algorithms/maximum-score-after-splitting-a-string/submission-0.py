class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        c = float("-inf")
        for i in range(1, len(s)):
            L = s[:i]
            R = s[i:]
            count_L = Counter(L)
            count_R = Counter(R)
            c = max(c, count_L["0"] + count_R["1"])
        return c