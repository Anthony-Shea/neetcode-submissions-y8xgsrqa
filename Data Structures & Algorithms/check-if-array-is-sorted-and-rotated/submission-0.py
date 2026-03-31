class Solution:
    def check(self, nums: List[int]) -> bool:
        s = sorted(nums)
        for i in range(len(nums)):
            if s == (nums[i%len(nums):] + nums[:i%len(nums)]):
                return True
        return False