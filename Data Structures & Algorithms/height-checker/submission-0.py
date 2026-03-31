class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        r = 0
        for a, b in zip(heights, s):
            if a != b:
                r += 1

        return r