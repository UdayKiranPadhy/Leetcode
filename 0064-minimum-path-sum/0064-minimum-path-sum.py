class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R , C = len(grid), len(grid[0])
        @cache
        def dfs(x,y):
            if (x,y) == (R-1,C-1):
                return grid[x][y]
            res = float('inf')
            for dx,dy in [[1,0],[0,1]]:
                nx , ny = x + dx, y + dy
                if 0<= nx < R and 0 <= ny < C:
                    res = min(res,grid[x][y] + dfs(nx,ny))
            return res
        return dfs(0,0)