class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        m = {}
        for i in range(len(keyboard)):
            m[keyboard[i]] = i

        prev = 0
        result = 0
        for c in word:
            result += abs(prev - m[c])
            prev = m[c]
        return result
