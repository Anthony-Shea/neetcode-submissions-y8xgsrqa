class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] < k:
                        res = max(res, nums[i] + nums[j])
        return res