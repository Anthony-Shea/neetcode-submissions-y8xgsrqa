class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        r = 0
        n = 0
        for i in range(len(weight)):
            if i == 0:
                r = weight[i]
                n = 1
            else:
                if r + weight[i] > 5000:
                    return n
                else:
                    n += 1
                    r += weight[i]
        return n