class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = {}
        l = -1
        for n in arr:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1           
        for n in m:
            if m[n] == n and n > l:
                l = n
        return l