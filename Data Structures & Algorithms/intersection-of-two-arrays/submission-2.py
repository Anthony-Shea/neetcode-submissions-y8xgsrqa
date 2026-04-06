class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s, r = set(nums1), []
        for n in nums2:
            if n in s:
                r.append(n), s.remove(n)
        return r