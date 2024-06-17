class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.current = 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.current = 0
            return False
        self.current += 1
        return self.current >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)