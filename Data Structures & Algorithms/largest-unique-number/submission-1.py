class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort(reverse=True)
        currentIndex = 0
        while currentIndex < n:
            if currentIndex == n - 1 or nums[currentIndex] != nums[currentIndex + 1]:
                return nums[currentIndex]
            while currentIndex < n - 1 and nums[currentIndex] == nums[currentIndex +1]:
                currentIndex += 1

            currentIndex += 1
        return -1