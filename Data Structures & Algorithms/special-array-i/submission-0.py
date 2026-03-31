class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        b = 0
        if len(nums) == 1:
            return True
        for num in nums:
            if b == False:
                if num % 2 == 0:
                    b = True
                    continue
                else:
                    return False
            elif b == True:
                if num % 2 != 0:
                    b = False
                    continue
                else:
                    return False
        return True