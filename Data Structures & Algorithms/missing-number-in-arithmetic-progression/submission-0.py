class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[n-1] - arr[0])//n
        l = 0
        h = n - 1
        while l < h:
            m = (l + h) // 2
            if arr[m] == arr[0] + m * d:
                l = m + 1
            else:
                h = m
        return arr[0] + d * l