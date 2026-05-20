class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            m1[s[i]]+= 1
            m2[t[i]] += 1
        return m1 == m2