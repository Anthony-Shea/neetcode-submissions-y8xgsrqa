class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in ms:
                ms[s[i]] += 1
            if s[i] not in ms:
                ms[s[i]] = 1
            if t[i] in mt:
                mt[t[i]] += 1
            if t[i] not in mt:
                mt[t[i]] = 1
        return ms == mt