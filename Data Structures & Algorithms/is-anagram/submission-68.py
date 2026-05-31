class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        for a, b in zip(s,t):
            if a != b:
                return False
        if len(s) != len(t):
            return False
        return True