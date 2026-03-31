class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incCur = 1
        incMax = 1
        decCur = 1
        decMax = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                incCur += 1
                incMax = max(incCur, incMax)
                decCur = 1
            elif nums[i] > nums[i+1]:
                decCur += 1
                decMax = max(decCur, decMax)
                incCur = 1
            else:
                decCur = 1
                incCur = 1
        return max(incMax, decMax)