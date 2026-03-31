class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        m = 0
        for l in arr:
            if c[l] > 1:
                continue
            m += 1
            if m == k:
                return l
        return ""