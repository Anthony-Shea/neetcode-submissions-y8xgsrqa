class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        for i in range(len(mat)):
            r += mat[i][len(mat) - i - 1]
            r += mat[i][i]
        return r - (mat[len(mat) // 2][len(mat) // 2] if len(mat) % 2 else 0)