class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        @cache
        def go(index,prev):
            if index == N:
                return 0
            best = float('inf')
            for j in range(len(grid[index])):
                if j == prev:
                    continue
                best = min(best, grid[index][j] + go(index+1, j))
            return best
        return go(0,-1)