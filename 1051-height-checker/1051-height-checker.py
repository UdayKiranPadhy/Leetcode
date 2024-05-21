class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return len([x for x,y in zip(expected,heights) if x!=y])