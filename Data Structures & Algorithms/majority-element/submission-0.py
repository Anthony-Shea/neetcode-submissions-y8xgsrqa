class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1

        for num in m:
            print(num)
            print(m[num])
            if m[num] >= len(nums)/2:
                return num