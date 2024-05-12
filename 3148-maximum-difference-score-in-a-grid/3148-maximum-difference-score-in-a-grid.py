class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        M , N = len(grid), len(grid[0])
        cache = [[None for i in range(N)] for j in range(M)]
        gg = -float('inf')
        def go(i,j):
            nonlocal gg
            if cache[i][j]:
                return cache[i][j]
            if i == M-1 and j == N-1:
                return 0
            right = down = float('-inf')
            if j + 1 < N:
                right = grid[i][j+1] - grid[i][j] + go(i,j+1)
            if i + 1 < M:
                down = grid[i+1][j] - grid[i][j] + go(i+1,j)
            gg = max(gg,right,down)
            cache[i][j] = max(right, down,0)
            return max(cache[i][j],0)
        go(0,0)
        cache[M-1][N-1] = float('-inf')
        ans = max([max(i) for i in cache])
        return ans if ans != 0 else gg