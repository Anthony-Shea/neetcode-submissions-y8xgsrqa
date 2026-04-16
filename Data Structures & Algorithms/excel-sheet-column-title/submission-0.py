class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            r += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26
        return r[::-1]