class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        result = ""
        j = 1
        for char in t:
            if j > len(s):
                break
            if char == s[j-1]:
                result += char
                j += 1
        if result == s:
            return True
        return False