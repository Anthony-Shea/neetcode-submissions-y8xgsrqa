class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 1
        if nums[i-1] == nums[i]:
            while i != len(nums)-2 and nums[i-1] == nums[i]:
                i += 1
        if nums[i-1] < nums[i]:
            for i in range(i, len(nums)):
                if nums[i-1] <= nums[i]:
                    continue
                else:
                    return False
        elif nums[i-1] > nums[i]:
            for i in range(i, len(nums)):
                if nums[i-1] >= nums[i]:
                    continue
                else:
                    return False
        return True