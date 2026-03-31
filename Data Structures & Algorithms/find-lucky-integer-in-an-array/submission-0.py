class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = defaultdict(int)
        l = -1

        for n in arr:
            m[n] += 1
            
        for n in m:
            if m[n] == n and n > l:
                l = n
        return l