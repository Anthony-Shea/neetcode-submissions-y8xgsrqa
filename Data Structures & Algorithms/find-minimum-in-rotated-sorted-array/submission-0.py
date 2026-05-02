class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = float('inf')
        for i in range(len(nums)):
            m = min(m, nums[i])
        return m