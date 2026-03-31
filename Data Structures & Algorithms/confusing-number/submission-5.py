class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated = ""
        valid = {0: 0,
                1: 1,
                6: 9,
                8: 8,
                9: 6
                }
        num = str(n)
        for i, char in reversed(list(enumerate(num))):
            if int(char) in valid:
                rotated += str(valid[int(char)])
            else:
                return False
        if int(rotated) == n:
            return False
        return True