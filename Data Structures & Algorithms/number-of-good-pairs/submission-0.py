class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        r = 0
        c = Counter(nums)
        for n in c:
            c[n] -= 1
            r += (c[n]*(c[n] + 1))/2
        return int(r)