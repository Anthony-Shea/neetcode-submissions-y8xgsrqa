class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r = r | n
        r <<= len(nums) - 1
        return r