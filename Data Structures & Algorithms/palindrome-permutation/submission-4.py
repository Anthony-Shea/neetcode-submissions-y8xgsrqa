class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        for i in range(128):
            if count > 1:
                break
            ct = 0
            for j in range(len(s)):
                if s[j] == chr(i):
                    ct += 1

            count += ct % 2
        return count <= 1