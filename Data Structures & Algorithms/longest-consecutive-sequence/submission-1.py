class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        r = 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i] - 1 and nums[i-1] != nums[i]:
                cur = 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                cur += 1
                r = max(r, cur)
        return r