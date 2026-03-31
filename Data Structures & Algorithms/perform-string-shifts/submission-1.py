class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        k = 0
        for shif in shift:
            if shif[0] == 1:
                k += shif[1]
            if shif[0] == 0:
                k -= shif[1]
        k = k % len(s)
        return s[-k:] + s[:-k]