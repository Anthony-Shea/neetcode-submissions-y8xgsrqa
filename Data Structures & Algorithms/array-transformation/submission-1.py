class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        ops = 1
        while ops:
            ops = 0
            a = arr[:]
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    a[i] += 1
                    ops += 1
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    a[i] -= 1
                    ops += 1
            arr = a
        return arr
