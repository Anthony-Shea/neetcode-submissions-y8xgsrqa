class Logger:

    def __init__(self):
        self.m = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if len(self.m) == 0:
            self.m[message] = timestamp + 10
            return True
        else:
            if message in self.m and timestamp < self.m[message]:
                return False
            else:
                self.m[message] = timestamp + 10
                return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
