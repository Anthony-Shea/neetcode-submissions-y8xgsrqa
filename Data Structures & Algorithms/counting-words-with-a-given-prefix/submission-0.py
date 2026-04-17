class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        r = 0
        for w in words:
            if w.startswith(pref):
                r += 1
        return r