class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = []
        repeats = []
        for arr in grid:
            for num in arr:
                if num in values:
                    repeats.append(num)
                values.append(num)
        s = set(range(1, len(values) + 1))
        for value in values:
            s.discard(value)
        res = []
        res.extend(repeats)
        res.extend(list(s))
        return res
        