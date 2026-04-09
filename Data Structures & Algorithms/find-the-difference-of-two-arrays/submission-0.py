class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m1 = {}
        m2 = {}
        for n in nums1:
            if n not in m1:
                m1[n] = True
            else:
                continue
        for n in nums2:
            if n not in m2:
                m2[n] = True
            else:
                continue
        r1 = []
        r2 = []
        print(m1)
        print(m2)
        for n in m1:
            if n not in m2:
                r1.append(n)
        for n in m2:
            if n not in m1:
                r2.append(n)
        r = [r1, r2]
        return r