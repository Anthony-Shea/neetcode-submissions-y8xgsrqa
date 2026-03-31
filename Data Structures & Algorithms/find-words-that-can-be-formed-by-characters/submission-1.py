class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        r = 0
        for w in words:
            c = Counter(chars)
            length = len(w)
            for l in w:
                if l in c and c[l] > 0:
                    c[l] -= 1
                    length -= 1
                else:
                    break
                if length == 0:
                    r += len(w)
        return r
                