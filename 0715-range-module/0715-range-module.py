class RangeModule:

    def __init__(self):
        self.track = []
        

    def addRange(self, left: int, right: int) -> None:
        start = bisect_left(self.track,left)
        end = bisect_right(self.track,right)

        subtrack = []
        if start%2 == 0:
            subtrack.append(left)
        if end %2 == 0:
            subtrack.append(right)
        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect_right(self.track,left)
        end = bisect_left(self.track,right)

        return start == end and start % 2 == 1
        # [1, 5, 7, 10, 20, 30]

    def removeRange(self, left: int, right: int) -> None:
        start = bisect_left(self.track,left)
        end = bisect_right(self.track,right)

        subtrack = []
        if start %2 == 1:
            subtrack.append(left)
        if end %2 == 1:
            subtrack.append(right)
        self.track[start:end] = subtrack
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)