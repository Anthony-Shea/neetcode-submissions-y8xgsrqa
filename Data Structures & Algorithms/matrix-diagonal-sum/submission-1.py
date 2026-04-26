class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        for i in range(len(mat)):
            r += mat[i][i]
        for i in range(len(mat)):
            j = len(mat) - i - 1
            r += mat[i][j]
            if i == j:
                r -= mat[i][j]
        return r