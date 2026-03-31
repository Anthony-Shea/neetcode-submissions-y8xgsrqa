class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i, l in enumerate(pattern):
            if l not in m and s[i] not in m:
                m[l] = s[i]
                m[s[i]] = l
                print(m)
            else:
                if l not in m:
                    return False
                if m[l] != s[i]:
                    return False
        return True