class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def genRow(prev):
            r = [1] * (len(prev) + 1)
            if len(prev) > 1:
                for i in range(1, len(prev)):
                    r[i] = prev[i-1] + prev[i]
            return r

        result = []
        for i in range(numRows):
            if i == 0:
                initial_row = genRow([])
                prev = initial_row
                result.append(prev)
            else:
                prev = genRow(prev)
                result.append(prev)
        return result


            