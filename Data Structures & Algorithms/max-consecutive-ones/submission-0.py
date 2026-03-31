class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            if curr > r:
                r = curr
        return r