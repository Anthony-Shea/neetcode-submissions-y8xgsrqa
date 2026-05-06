class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while l < r:
            print("here")
            print(l)
            print(r)
            print(m)
            if m%2==0 and nums[m] == nums[m-1]:
                r = m - 1
            elif m%2==0 and nums[m] == nums[m+1]:
                l = m + 1
            elif m%2==0:
                return nums[m]
            elif m%2 and nums[m] == nums[m-1]:
                l = m + 1
            elif m%2 and nums[m] == nums[m+1]:
                r = m - 1
            else:
                return nums[m]
            m = (l + r) // 2
        return nums[m]