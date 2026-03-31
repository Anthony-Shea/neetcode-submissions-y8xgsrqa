class Solution:
    def countSeniors(self, details: List[str]) -> int:
        r = 0
        for d in details:
            if int(d[11:13]) > 60:
                r += 1

        return r