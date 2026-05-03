class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            a = arrays[i]
            res = max(res, max(a[-1]-cur_min,cur_max-a[0]))
            cur_min = min(cur_min, a[0])
            cur_max = max(cur_max, a[-1])
        return res