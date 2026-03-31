class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    temp[i] *= nums[j]
        return temp