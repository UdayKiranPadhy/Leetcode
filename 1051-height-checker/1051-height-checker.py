class Solution:
    def heightChecker(self, H):
        return sum(x != y for x, y in zip(H, sorted(H)))