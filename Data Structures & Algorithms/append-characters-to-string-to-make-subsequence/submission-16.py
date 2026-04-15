class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l1, l2 = 0, 0
        cnt = 0
        best = ""
        cur = ""
        while l1 < len(s) and l2 < len(t):
            if s[l1] == t[l2]:
                cur += s[l1]
                cnt += 1
                if len(cur) > len(best):
                    best = cur
                else:
                    best += cur
                l2 += 1
            else:
                cur = ""
            l1 += 1
        return len(t) - cnt