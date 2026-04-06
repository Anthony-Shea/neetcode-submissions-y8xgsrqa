class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        for n in nums1:
            s.add(n)
        r = []
        for n in nums2:
            if n in s:
                r.append(n)
                s.remove(n)
        return r