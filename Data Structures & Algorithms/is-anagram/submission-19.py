class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        c2 = Counter(t)
        return c == c2