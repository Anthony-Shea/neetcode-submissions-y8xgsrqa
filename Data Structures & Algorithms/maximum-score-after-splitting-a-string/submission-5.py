class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        c = 0
        for i in range(1, len(s)):
            L = s[:i]
            R = s[i:]
            c_L = Counter(L)
            c_R = Counter(R)
            c = max(c, c_L["0"] + c_R["1"])
        return c