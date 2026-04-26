class Solution:
    def maxDepth(self, s: str) -> int:
        r = 0
        m = []
        b = 0
        for i, c in enumerate(s):
            if c == "(":
                r += 1
            elif c == ")":
                r -= 1
            b = max(b, r)
        return b