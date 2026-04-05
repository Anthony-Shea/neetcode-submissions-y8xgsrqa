class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        m = {}
        for w in words:
            for c in w:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
        for c in m:
            if m[c] % len(words) != 0:
                return False
        return True
