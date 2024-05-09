class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x , y = point
        self.points.setdefault((x, y) , 0)
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x , y in self.points.keys():
            if px == x and py == y: continue
            if (x,py) in self.points and (px,y) in self.points and abs(py-y) == abs(px-x):
                res += self.points[(x,py)] * self.points[(px,y)] * self.points[(x,y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)