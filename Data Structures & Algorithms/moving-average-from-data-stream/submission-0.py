class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = []
        self.avg = 0
        self.length = 0

    def next(self, val: int) -> float:
        if len(self.nums) == 0:
            self.nums.append(val)
            self.avg = val
            self.length = 1
        elif len(self.nums) < self.size:
            self.nums.append(val)
            self.length += 1
            self.avg = sum(self.nums) / self.length
        else:
            self.nums.append(val)
            self.length += 1
            self.avg = 0
            for i in range(-1, -1 - self.size, -1):
                self.avg += self.nums[i]
            self.avg /= self.size
        return float(self.avg)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
