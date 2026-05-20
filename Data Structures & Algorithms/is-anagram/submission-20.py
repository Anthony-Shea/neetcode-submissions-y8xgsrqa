class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in m1:
                m1[s[i]] = 1
            if s[i] in m1:
                m1[s[i]]+= 1
            if t[i] not in m2:
                m2[t[i]] = 1
            if t[i] in m2:
                m2[t[i]] += 1
        return m1 == m2