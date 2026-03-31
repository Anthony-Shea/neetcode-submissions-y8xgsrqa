class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i, num1 in enumerate(nums1):
            if num1 in nums2:
                index_num = nums2.index(num1)
                result.append(index_num)

        return result