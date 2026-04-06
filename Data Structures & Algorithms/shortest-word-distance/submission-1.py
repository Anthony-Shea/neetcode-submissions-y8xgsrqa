class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        m = {}
        for i, w in enumerate(wordsDict):
            if w not in m:
                m[w] = [i]
            else:
                m[w].append(i)
        d = len(wordsDict)
        for i in m[word1]:
            for j in m[word2]:
                d = min(d, abs(i - j))
        return d