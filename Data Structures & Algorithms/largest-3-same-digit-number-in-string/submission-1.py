class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        l = float("-inf")
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                g = num[i-2] + num[i-1] + num[i]
                l = max(l, int(g))
        if l != float("-inf"):
            res = str(l)
            if res == "0":
                res = "000"
        return res