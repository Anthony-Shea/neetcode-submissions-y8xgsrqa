class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {n:i for i, n in enumerate(nums1)}
        r = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = m[val]
                r[idx] = cur
            if cur in m:
                stack.append(cur)
        return r