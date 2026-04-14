class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        c = Counter(nums)
        for n in c:
            if c[n] > len(nums) / 2 and n == target:
                return True
        return False