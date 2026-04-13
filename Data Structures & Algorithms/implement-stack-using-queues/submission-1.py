class MyStack:

    def __init__(self):
        from queue import Queue
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        for i in range(self.q.qsize() - 1):
            self.push(self.q.get())
        return self.q.get()

    def top(self) -> int:
        val = self.pop()
        self.push(val)
        return val

    def empty(self) -> bool:
        return self.q.qsize() == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()