class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i, char in enumerate(s):
            if i < len(s)-1:
                result += abs(ord(s[i+1]) - ord(s[i]))
        return result