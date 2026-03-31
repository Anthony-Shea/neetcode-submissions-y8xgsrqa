class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best=nums[0]
        curr=nums[0]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                curr += nums[i+1]
                if curr > best:
                    best = curr
            else:
                curr = nums[i+1]
        return best