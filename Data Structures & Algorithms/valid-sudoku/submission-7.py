class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            m1 = {}
            for num in row:
                if num in m1 and num != ".":
                    return False
                else:
                    m1[num] = True
        for i in range(9):
            m2 = {}
            for j in range(9):
                if board[j][i] in m2 and board[j][i] != ".":
                    return False
                else:
                    m2[board[j][i]] = True
        m3 = {}
        for i in range(3):
            for j in range(3):
                if board[i][j] in m3 and board[i][j] != ".":
                    return False
                else:
                    m3[board[i][j]] = True
        m3 = {}
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] in m3 and board[i][j] != ".":
                    return False
                else:
                    m3[board[i][j]] = True
        m3 = {}
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] in m3 and board[i][j] != ".":
                    return False
                else:
                    m3[board[i][j]] = True
        m3 = {}
        for i in range(3):
            for j in range(3,6):
                if board[i][j] in m3 and board[i][j] != ".":
                    return False
                else:
                    m3[board[i][j]] = True
        m3 = {}
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] in m3 and board[i][j] != ".":
                    return False
                else:
                    m3[board[i][j]] = True
        m3 = {}
        for i in range(6,9):
            for j in range(3):
                if board[i][j] in m3 and board[i][j] != ".":
                    return False
                else:
                    m3[board[i][j]] = True
        return True