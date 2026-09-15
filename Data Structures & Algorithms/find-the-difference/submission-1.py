class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ""
        s = Counter(s)
        t = Counter(t)
        for c in t:
            if c not in s or t[c] != s[c]:
                res = c
        return res