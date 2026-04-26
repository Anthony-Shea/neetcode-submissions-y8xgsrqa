class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        n = r = 0
        for w in weight:
            r += w
            if r > 5000:
                break
            n += 1
        return n