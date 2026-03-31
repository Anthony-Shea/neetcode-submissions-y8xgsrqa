class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = []
        c = Counter(nums)
        for i in range(k):
            val = max(c, key=c.get)
            r.append(val)
            del c[val]
        return r