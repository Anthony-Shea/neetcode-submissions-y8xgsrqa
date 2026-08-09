class Solution:
    def countLetters(self, s: str) -> int:
        total = left = 0
        for right in range(len(s) + 1):
            if right == len(s) or s[left] != s[right]:
                len_substring = right - left
                total += (1 + len_substring) * len_substring // 2
                left = right
        return total