class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.incr = []
        self.N = maxSize

    def push(self, x: int) -> None:
        if self.N > len(self.stack):
            self.stack.append(x)
            self.incr.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        self.prev = self.incr[-1]
        if len(self.incr) > 1:
            self.incr[-2] += self.prev
        return self.stack.pop() + self.incr.pop()

    def increment(self, k: int, val: int) -> None:
        self.incr[min(k-1,len(self.incr)-1)] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)