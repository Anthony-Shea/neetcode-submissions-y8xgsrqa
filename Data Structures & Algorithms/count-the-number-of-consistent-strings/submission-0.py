class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        r = 0
        for word in words:
            i = 0
            for letter in word:
                if letter not in allowed:
                    break
                i += 1
            if i == len(word):
                r += 1
        return r