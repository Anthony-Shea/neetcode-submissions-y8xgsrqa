class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = 0
        square = 0
        for s in students:
            if s == 0:
                circle += 1
            elif s == 1:
                square += 1
        for s in sandwiches:
            if s == 0:
                if circle > 0:
                    circle -= 1
                else:
                    break
            if s == 1:
                if square > 0:
                    square -=1
                else:
                    break
        return circle + square