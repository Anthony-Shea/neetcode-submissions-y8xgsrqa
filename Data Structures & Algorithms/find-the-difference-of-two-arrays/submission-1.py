class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        r1 = []
        r2 = []
        for n in s1:
            if n not in s2:
                r1.append(n)
        for n in s2:
            if n not in s1:
                r2.append(n)
        return [r1,r2]