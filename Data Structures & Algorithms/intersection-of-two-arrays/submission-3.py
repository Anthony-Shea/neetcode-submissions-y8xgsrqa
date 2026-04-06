class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s, r = set(nums1), []
        [r.append(n) or s.remove(n) for n in nums2 if n in s]
        return r