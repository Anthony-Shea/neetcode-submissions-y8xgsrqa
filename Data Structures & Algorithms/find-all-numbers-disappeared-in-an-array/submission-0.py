class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        res = []
        for i in range(1, len(nums)+1):
            if m[i] == 0:
                res.append(i)
        return res
