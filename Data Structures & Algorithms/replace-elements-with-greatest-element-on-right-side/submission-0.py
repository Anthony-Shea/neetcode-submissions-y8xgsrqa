class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        result.append(-1)
        i = len(arr) - 1
        largest_so_far = -1
        while i > 0:
            if arr[i] > largest_so_far:
                largest_so_far = arr[i]
            result.insert(0, largest_so_far)
            i -= 1
        return result
