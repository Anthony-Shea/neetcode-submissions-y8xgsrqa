class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        m = {}
        for arr in grid:
            for value in arr:
                if value in m:
                    res.append(value)
                else:
                    m[value] = 1
        for i in range(1, len(m)+2):
            if i not in m:
                res.append(i)
        return res